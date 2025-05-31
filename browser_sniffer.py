from playwright.sync_api import sync_playwright

def get_video_urls_from_page(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        page.goto(url, wait_until="networkidle")  # Wait for all requests to settle
        page.wait_for_timeout(2000)  # Small buffer wait

        # Collect all video srcs (from <video> and <source> tags)
        video_urls = page.eval_on_selector_all(
            "video, source",
            "elements => elements.map(e => e.src).filter(src => src)"
        )

        browser.close()
        return video_urls

