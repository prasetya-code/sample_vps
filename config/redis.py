import redis, os

# ==========================
# Konfigurasi Redis Production
# ==========================
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 2))    # 2 especialy for rate limitter
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)

# Build Redis URI untuk Flask-Limiter
if REDIS_PASSWORD:
    REDIS_URI = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"
    
else:
    REDIS_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}"

# Redis client untuk akses manual jika diperlukan
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    password=REDIS_PASSWORD,
    decode_responses=True
)