"""
QR Code Generator Application
Generates QR codes from URLs and saves them to the qr_codes/ directory.
Supports configuration via command-line arguments and environment variables.
"""

import argparse
import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import qrcode

# ── Logging setup ──────────────────────────────────────────────────────────────
LOG_DIR = Path(os.getenv("LOG_DIR", "logs"))
QR_DIR  = Path(os.getenv("QR_CODE_DIR", "qr_codes"))

LOG_DIR.mkdir(parents=True, exist_ok=True)
QR_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOG_DIR / "qr_generator.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


# ── Argument parsing ───────────────────────────────────────────────────────────
def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a QR code image from a URL."
    )
    parser.add_argument(
        "--url",
        type=str,
        default=os.getenv("QR_URL", "https://github.com/kaw393939"),
        help="URL to encode in the QR code (default: https://github.com/kaw393939)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output filename (without extension). Defaults to a timestamp-based name.",
    )
    parser.add_argument(
        "--fill-color",
        type=str,
        default=os.getenv("QR_FILL_COLOR", "black"),
        help="Foreground color of the QR code (default: black)",
    )
    parser.add_argument(
        "--back-color",
        type=str,
        default=os.getenv("QR_BACK_COLOR", "white"),
        help="Background color of the QR code (default: white)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=int(os.getenv("QR_SIZE", "10")),
        help="Box size in pixels per module (default: 10)",
    )
    parser.add_argument(
        "--border",
        type=int,
        default=int(os.getenv("QR_BORDER", "4")),
        help="Border width in modules (default: 4)",
    )
    return parser.parse_args()


# ── QR code generation ─────────────────────────────────────────────────────────
def generate_qr_code(url, output_path, fill_color, back_color, box_size, border):
    """Generate a QR code PNG for url and save it to output_path."""
    logger.info("Generating QR code for URL: %s", url)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(output_path)

    logger.info("QR code saved to: %s", output_path)


# ── Entry point ────────────────────────────────────────────────────────────────
def main():
    args = parse_args()

    if args.output:
        filename = f"{args.output}.png"
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"qr_{timestamp}.png"

    output_path = QR_DIR / filename

    try:
        generate_qr_code(
            url=args.url,
            output_path=output_path,
            fill_color=args.fill_color,
            back_color=args.back_color,
            box_size=args.size,
            border=args.border,
        )
        logger.info("Done! QR code generated successfully.")
    except Exception as exc:
        logger.error("Failed to generate QR code: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
