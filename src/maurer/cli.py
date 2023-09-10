"""CLI handling helpers for Maurer."""

import argparse
from .engine import generate_site
from .server import run_server


def run_from_cli():
    parser = argparse.ArgumentParser(description="Generate a static site.")

    parser.add_argument("template", help="The template file path (e.g. template.html)")
    parser.add_argument("posts", help="The content directory path (e.g. /articles)")
    parser.add_argument(
        "-o", "--output", help="The build directory path (e.g. build)", default="build"
    )
    parser.add_argument("-w", "--watch", help="Watch for changes", action="store_true")
    args = parser.parse_args()
    print("\033[94m" + "Generating site..." + "\033[0m")
    generate_site(args.template, args.posts, args.output)
    print("\033[92m" + "Site is ready in /" + args.output + "\033[0m")
    if args.watch:
        print("\033[94m" + "Watching for changes..." + "\033[0m")
        run_server(
            args.articles,
            lambda: generate_site(args.template, args.posts, args.output),
        )
