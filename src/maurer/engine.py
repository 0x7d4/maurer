"""Core generation engine for Maurer."""


import os


def generate_site(template_file, articles_dir, build_dir):
    # Read the template content from the file
    with open(template_file, "r") as template:
        template_content = template.read()

    # Create the build directory if it doesn't exist
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    # Iterate over HTML articles in the articles directory
    for article_filename in os.listdir(articles_dir):
        if article_filename.endswith(".html"):
            # Read the content of the article
            with open(
                os.path.join(articles_dir, article_filename), "r"
            ) as article_file:
                article_content = article_file.read()

            # Get the article title from the filename
            article_title = os.path.splitext(article_filename)[0]

            # Replace <view></view> with article content in the template
            page_content = template_content.replace(
                "<view></view>",
                f"<article><h1>{article_title}</h1>\n{article_content}</article>",
            )

            # Create the output filename based on the article title
            output_filename = os.path.join(
                build_dir, f"{article_title.lower().replace(' ', '-')}.html"
            )

            # Write the page content to the output HTML file
            with open(output_filename, "w") as output_file:
                output_file.write(page_content)
