#!/usr/bin/env python3
"""
Bọc mảnh HTML của artifact thành một trang HTML hoàn chỉnh cho GitHub Pages.

Vì sao cần script này thay vì copy tay:
  `documents/bao-cao-boi-canh.html` được viết cho Artifact, nơi nền tảng tự bọc
  <!doctype>/<html>/<head>/<body> và tự thêm <meta charset>. GitHub Pages không làm vậy.
  Thiếu charset thì toàn bộ tiếng Việt vỡ dấu; thiếu doctype thì trình duyệt vào
  quirks mode và box-sizing chạy sai.

  Giữ một nguồn duy nhất (file trong documents/) rồi sinh ra docs/index.html,
  để sửa một chỗ là cả artifact lẫn trang web cùng cập nhật.

Dùng:
    python3 scripts/build-site.py
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "documents" / "bao-cao-boi-canh.html"
OUT_DIR = ROOT / "docs"
OUT = OUT_DIR / "index.html"

# Đổi thành domain thật nếu dùng custom domain
SITE_URL = "https://thinhsuy.github.io/resort-management-agency/"


def main() -> int:
    if not SRC.exists():
        print(f"Không tìm thấy file nguồn: {SRC}", file=sys.stderr)
        return 1

    fragment = SRC.read_text(encoding="utf-8")

    title_match = re.search(r"<title>(.*?)</title>", fragment, re.S)
    desc_match = re.search(
        r'<meta name="description" content="([^"]*)"', fragment
    )
    if not title_match:
        print("Mảnh HTML không có <title> — dừng.", file=sys.stderr)
        return 1

    title = title_match.group(1).strip()
    description = desc_match.group(1).strip() if desc_match else ""

    # Bỏ <title>/<meta> khỏi phần thân vì chúng được đặt lại trong <head>
    body = fragment
    body = re.sub(r"<title>.*?</title>\s*", "", body, count=1, flags=re.S)
    body = re.sub(
        r'<meta name="description"[^>]*>\s*', "", body, count=1
    )
    body = body.strip()

    page = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="robots" content="noindex, nofollow">

<meta property="og:type" content="article">
<meta property="og:locale" content="vi_VN">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_URL}">
<meta name="twitter:card" content="summary">

<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🏝️</text></svg>">

<!-- Trang này được sinh tự động bởi scripts/build-site.py — đừng sửa trực tiếp.
     Sửa documents/bao-cao-boi-canh.html rồi chạy lại script. -->
</head>
<body>
{body}
</body>
</html>
"""

    OUT_DIR.mkdir(exist_ok=True)
    OUT.write_text(page, encoding="utf-8")

    # .nojekyll: bỏ qua bước xử lý Jekyll (nhanh hơn, và không nuốt file bắt đầu bằng _)
    (OUT_DIR / ".nojekyll").write_text("", encoding="utf-8")

    print(f"✓ Đã tạo {OUT.relative_to(ROOT)}  ({OUT.stat().st_size:,} byte)")
    print(f"✓ Đã tạo {(OUT_DIR / '.nojekyll').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
