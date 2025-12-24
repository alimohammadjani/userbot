import os
import sqlite3
import time
from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import logging

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# تنظیمات تلگرام
api_id = 0
api_hash = ""
group = ""

# نام فایل دیتابیس
DB_NAME = "telegram_members.db"


def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            phone TEXT,
            is_bot BOOLEAN,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()
    logging.info("دیتابیس آماده است")


def save_member_to_db(member):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT OR REPLACE INTO members 
            (user_id, username, first_name, last_name, phone, is_bot)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            member.id,
            member.username or None,
            member.first_name or None,
            member.last_name or None,
            getattr(member, 'phone', None),
            getattr(member, 'bot', False)
        ))
        
        conn.commit()
    except Exception as e:
        logging.error(f"خطا در ذخیره کاربر {member.id}: {e}")
    finally:
        conn.close()


def export_members_to_database():
    if not api_id or not api_hash or group == "examplegroup":
        raise ValueError("لطفاً api_id، api_hash و لینک گروه را درست وارد کنید")

    init_database()

    with TelegramClient("session_name", api_id, api_hash) as client:
        try:
            entity = client.get_entity(group)
            
            participants = client.get_participants(entity, aggressive=True)
            
            total = len(participants)
            
            saved_count = 0
            for i, p in enumerate(participants, 1):
                save_member_to_db(p)
                saved_count += 1
                
                if i % 50 == 0:
                    logging.info(f"پیشرفت: {i}/{total} ({(i/total)*100:.1f}%)")
            logging.info(f"تعداد کاربران ذخیره شده در دیتابیس: {saved_count}")
            logging.info(f"فایل دیتابیس: {os.path.abspath(DB_NAME)}")
            
        except FloodWaitError as e:
            logging.warning(f"محدودیت تلگرام! باید {e.seconds} ثانیه صبر کنیم...")
            time.sleep(e.seconds)
        except Exception as ex:
            logging.error(f"خطای کلی رخ داد: {ex}")


if __name__ == "__main__":
    export_members_to_database()