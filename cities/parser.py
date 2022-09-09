import argparse

def init_parser():
    """
    parser initialization
    """
    parser = argparse.ArgumentParser(description="")
    
    parser.add_argument('city', type=str, help='city name')
    return parser