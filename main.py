import argparse

from config import compact_cfg, load_cfg
from engine.mail import Mail


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, help='Config Name', default='DEFAULT_CFG')
    parser.add_argument('--mail.host', type=str, help='Mail Host', required=True)
    parser.add_argument('--mail.username', type=str, help='Mail Username', required=True)
    parser.add_argument('--mail.password', type=str, help='Mail Password', required=True)
    parser.add_argument('--mail.to', type=str, help='Mail Send to', required=True)
    args = parser.parse_args()

    cfg = load_cfg(args.config)
    del args.config
    cfg = compact_cfg(cfg, args)

    mail = Mail(cfg.mail)
    mail.send('Test', ['Hello!', 'This is a test message.'])


if __name__ == '__main__':
    main()
