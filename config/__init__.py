def register_config(app): 
    from config.logger import setup_logger
    import os

    # Set Logger
    logger = setup_logger()

    # Hanya log "Restart" ketika proses utama berjalan setelah restart
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        boundary = "="  * 30

        logger.info(f"\n{boundary} LOGGER STARTING POINT {boundary} \n")
        logger.info("Flask is restarting...")
        logger.info("Log Start ... \n")


    # Set Static Ver
    from config.static_ver import apply_static_versioning
    apply_static_versioning(app)

    # Set Redis
    from config.redis import REDIS_URI, redis_client
    
    # Simpan di app.config agar bisa diakses dari route/module lain
    app.config['REDIS_URI'] = REDIS_URI
    app.config['REDIS_CLIENT'] = redis_client

    logger.info(f"Redis initialized: {REDIS_URI}")