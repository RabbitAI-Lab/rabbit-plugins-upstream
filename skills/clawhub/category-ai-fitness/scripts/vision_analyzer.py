"""
主图下载 + Claude 多模态视觉分析模块
对每张商品主图打 5 维度标签:
  1. background_type: white_pure / white_clean / lifestyle / studio / mixed
  2. has_brand_elements: 是否含品牌物/水印/logo/包装
  3. has_human: 是否含人物
  4. ai_difficulty: low / medium / high (AI改图难度)
  5. product_form: replacement_part / single_product / set / decoration / apparel / large_furniture / electronic / consumable
"""
import os
import json
import base64
import hashlib
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


CACHE_DIR = Path(__file__).parent.parent / "output" / "image_cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)
ANALYSIS_CACHE = Path(__file__).parent.parent / "output" / "vision_cache.json"


VISION_PROMPT = """You are an expert in e-commerce product photography and image content analysis. Analyze this product image and return ONLY a JSON object (no markdown, no explanation) with these exact fields:

{
  "background_type": "white_pure | white_clean | lifestyle | studio | mixed",
  "has_brand_elements": true/false,
  "brand_elements_detail": "describe what brand elements (logo/text/packaging) if any, else empty",
  "has_human": true/false,
  "human_detail": "hand_only | full_person | none",
  "has_text_watermark": true/false,
  "ai_difficulty": "low | medium | high",
  "ai_difficulty_reason": "brief reason: transparent/reflective/intricate-detail/needs-human/etc",
  "product_form": "replacement_part | single_product | set_bundle | decoration | apparel_textile | large_furniture | electronic_device | consumable | tool_hardware",
  "is_generic_supplier_image": true/false,
  "scene_fit_score": 0-100,
  "scene_fit_reason": "brief: does this product type benefit from lifestyle photography?"
}

Definitions:
- background_type:
  - white_pure: 100% pure white seamless background
  - white_clean: mostly white, slight shadow/gradient
  - lifestyle: real-life environment, room, outdoor, in-use scene
  - studio: styled prop background (color blocks, surfaces, props)
  - mixed: multi-panel image combining views
- has_brand_elements: visible brand logo, brand name text, branded packaging, or trademarked design
- ai_difficulty: how hard is it for AI to regenerate a lifestyle/scene version?
  - low: simple solid object, matte finish, no fine details
  - medium: some reflections/textures, moderate detail
  - high: transparent/glass, high-gloss reflective, intricate fine print, requires accurate human hand interaction
- product_form: classify the physical product
- is_generic_supplier_image: looks like a stock manufacturer image used by many sellers (white bg + multi-angle layout + text overlay)
- scene_fit_score: 0-100, how well would this product benefit from lifestyle/scene photography
  - 0-30: replacement parts, hardware, generic consumables (white bg always wins)
  - 31-60: small home goods, accessories (could go either way)
  - 61-100: furniture, decor, apparel, outdoor, kitchenware (lifestyle drives conversion)

Return ONLY the JSON object.
"""


def _load_cache() -> dict:
    if ANALYSIS_CACHE.exists():
        try:
            return json.loads(ANALYSIS_CACHE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def _save_cache(cache: dict):
    ANALYSIS_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def download_image(url: str, timeout: int = 20, max_retries: int = 3) -> bytes:
    """下载图片到本地缓存，返回 bytes（带重试 + 多 UA）"""
    if not url:
        return b""
    h = hashlib.md5(url.encode()).hexdigest()
    cache_path = CACHE_DIR / f"{h}.jpg"
    if cache_path.exists():
        return cache_path.read_bytes()

    uas = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    ]
    last_err = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, timeout=timeout, headers={
                "User-Agent": uas[attempt % len(uas)],
                "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
            })
            if resp.status_code == 200 and len(resp.content) > 1000:
                cache_path.write_bytes(resp.content)
                return resp.content
            last_err = f"HTTP {resp.status_code}"
        except Exception as e:
            last_err = str(e)
            time.sleep(0.5 * (attempt + 1))
    print(f"[Vision] 下载图片失败({max_retries}次重试) {url}: {last_err}", flush=True)
    return b""


def analyze_image(image_url: str, model: str = None) -> dict:
    """单张图片 → Claude 多模态分析 → 5 维度标签"""
    if not image_url:
        return {}

    cache = _load_cache()
    if image_url in cache:
        return cache[image_url]

    img_bytes = download_image(image_url)
    if not img_bytes:
        return {"error": "download_failed"}

    media_type = "image/jpeg"
    if image_url.lower().endswith(".png"):
        media_type = "image/png"
    elif image_url.lower().endswith(".webp"):
        media_type = "image/webp"

    try:
        import anthropic
    except ImportError:
        raise RuntimeError("缺少 anthropic 包，请先 pip install anthropic")

    client = anthropic.Anthropic(
        api_key=os.getenv("ANTHROPIC_AUTH_TOKEN") or os.getenv("ANTHROPIC_API_KEY"),
        base_url=os.getenv("ANTHROPIC_BASE_URL"),
    )

    model_name = model or os.getenv("ANTHROPIC_DEFAULT_HAIKU_MODEL") or "claude-haiku-4-5-20251001"

    img_b64 = base64.standard_b64encode(img_bytes).decode("utf-8")

    try:
        msg = client.messages.create(
            model=model_name,
            max_tokens=600,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "base64", "media_type": media_type, "data": img_b64},
                    },
                    {"type": "text", "text": VISION_PROMPT},
                ],
            }],
        )
        text = msg.content[0].text.strip()
        if text.startswith("```"):
            text = text.split("```", 2)[1]
            if text.startswith("json"):
                text = text[4:]
            text = text.rsplit("```", 1)[0].strip()
        result = json.loads(text)
        cache[image_url] = result
        _save_cache(cache)
        return result
    except json.JSONDecodeError as e:
        print(f"[Vision] JSON 解析失败: {e}, 原文: {text[:200]}", flush=True)
        return {"error": "parse_failed", "raw": text[:300]}
    except Exception as e:
        print(f"[Vision] 分析失败: {e}", flush=True)
        return {"error": str(e)}


def analyze_images_batch(image_urls: list, max_workers: int = 4) -> list:
    """并发分析一批图片，返回与输入顺序对齐的结果列表"""
    if not image_urls:
        return []
    results = [None] * len(image_urls)
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        future_to_idx = {ex.submit(analyze_image, url): i for i, url in enumerate(image_urls)}
        for fut in as_completed(future_to_idx):
            idx = future_to_idx[fut]
            try:
                results[idx] = fut.result()
            except Exception as e:
                results[idx] = {"error": str(e)}
            time.sleep(0.1)
    return results


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("用法: python3 vision_analyzer.py <image_url>")
        sys.exit(1)
    result = analyze_image(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
