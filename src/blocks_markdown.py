def markdown_to_blocks(markdown):
    parts = markdown.split('\n\n')

    res = []

    for part in parts:
        cleaned = part.strip()
        if cleaned != "":
            res.append(cleaned)

    return res