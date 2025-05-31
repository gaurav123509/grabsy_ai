from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

def get_video_urls_from_page(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            page.goto(url, wait_until="networkidle", timeout=10000)
            page.wait_for_timeout(2000)

            video_urls = page.eval_on_selector_all(
                "video, source",
                "elements => elements.map(e => e.src).filter(src => src)"
            )

            browser.close()
            return video_urls

    except PlaywrightTimeoutError:
        raise Exception("⏰ Timeout while loading the page")
    except Exception:
        raise  # preserves full traceback

