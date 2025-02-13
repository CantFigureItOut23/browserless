import os
from playwright.async_api import async_playwright
import random

async def main():
    proxies = [os.getenv(f'PROXY_{i}', '') for i in range(1, 10) if os.getenv(f'PROXY_{i}', '')]

    async with async_playwright() as p:
        if proxies:
            selected_proxy = random.choice(proxies)
            print(f"Using proxy: {selected_proxy}")
            browser = await p.chromium.launch({
                "proxy": {
                    "server": selected_proxy
                }
            })
        else:
            browser = await p.chromium.launch()  # No proxy

        # Here you would proceed with your Playwright operations
        context = await browser.new_context()
        page = await context.new_page()
        # Perform web scraping or other tasks with `page`
        
        await context.close()
        await browser.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    