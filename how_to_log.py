import logging

def setup_logging():
    '''
    Function to setup a logger
    '''
    logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True
    )

def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info(f"This is some info.")

if __name__ == "__main__":
    main()
