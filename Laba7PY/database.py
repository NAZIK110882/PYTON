import aiosqlite

DB_NAME = "bot_database.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                text TEXT NOT NULL
            )
        ''')
        await db.commit()

async def add_note(user_id: int, text: str):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("INSERT INTO notes (user_id, text) VALUES (?, ?)", (user_id, text))
        await db.commit()

async def get_notes(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT id, text FROM notes WHERE user_id = ?", (user_id,)) as cursor:
            return await cursor.fetchall()

async def delete_note(note_id: int, user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
        await db.commit()