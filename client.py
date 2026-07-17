class ContextDevScraperClient:
    def parse_html(self, raw_html: str) -> dict:
        # Mock regex tags stripping
        import re
        text = re.sub("<[^<]+?>", "", raw_html).strip()
        return {"extracted_text": text, "meta_description": "Cleaned article text"}