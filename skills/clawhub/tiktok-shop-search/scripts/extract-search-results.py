import argparse
import sys


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(description='Extract TikTok Shop search results from the current page SSR data.')
    parser.add_argument('--country_code', default='US', help='Country code (uppercase). Used to fill country_code field on each product.')
    args = parser.parse_args()

    country_code = args.country_code.upper().replace("'", "").replace('"', '')

    js = f"""
(function() {{
  try {{
    var script = document.getElementById('__MODERN_ROUTER_DATA__');
    if (!script) {{
      return JSON.stringify({{ error: true, message: 'SSR data script __MODERN_ROUTER_DATA__ not found. Page may not have finished loading or the URL is not a search results page.' }});
    }}
    var parsed;
    try {{ parsed = JSON.parse(script.textContent); }} catch (e) {{
      return JSON.stringify({{ error: true, message: 'Failed to parse SSR data: ' + e.message }});
    }}
    var page = parsed && parsed.loaderData && parsed.loaderData['(region)/(route_page_name)/page'];
    if (!page || !page.page_config || !Array.isArray(page.page_config.components_map)) {{
      return JSON.stringify({{ error: true, message: 'SSR structure unexpected: page_config.components_map missing.' }});
    }}
    var feed = page.page_config.components_map.find(function(c) {{ return c && c.component_name === 'feed_list_search_word'; }});
    if (!feed || !feed.component_data) {{
      return JSON.stringify({{ error: true, message: 'Search feed component (feed_list_search_word) not found on this page. Possible causes: (1) URL is not a search page; (2) region has no TikTok Shop coverage; (3) IP was blocked and captcha shown.' }});
    }}
    var cd = feed.component_data;
    var products = Array.isArray(cd.products) ? cd.products : [];
    var routeInfo = (page.route_info) || {{}};
    var keyword = routeInfo.keyword || routeInfo.route_keyword || null;

    function pickUrls(imgObj) {{
      if (!imgObj) return [];
      var out = [];
      if (imgObj.uri) out.push(imgObj.uri);
      if (Array.isArray(imgObj.url_list)) imgObj.url_list.forEach(function(u) {{ out.push(u); }});
      return out;
    }}

    function toNumber(v) {{
      if (v === null || v === undefined || v === '') return null;
      var n = Number(v);
      return isFinite(n) ? n : null;
    }}

    var items = products.map(function(p, idx) {{
      var priceInfo = p.product_price_info || {{}};
      var rate = p.rate_info || {{}};
      var sold = p.sold_info || {{}};
      var seller = p.seller_info || {{}};
      var seo = p.seo_url || {{}};
      var brand = p.brand_info || {{}};
      var skuList = Array.isArray(p.sku_info) ? p.sku_info : [];
      var currency = priceInfo.currency_name || null;
      var currencySymbol = priceInfo.currency_symbol || '';
      var salePrice = toNumber(priceInfo.sale_price_format);
      var originPrice = toNumber(priceInfo.origin_price_format);

      var skus = skuList.map(function(s) {{
        var pi = s.PriceInfo || {{}};
        return {{
          sku_id: s.SkuId || pi.sku_id || null,
          price: toNumber(pi.sale_price_format),
          price_str: pi.currency_symbol && pi.sale_price_format ? (pi.currency_symbol + pi.sale_price_format) : null,
          currency: pi.currency_name || null,
          origin_price: toNumber(pi.origin_price_format),
          discount_format: pi.discount_format || null
        }};
      }});

      return {{
        rank: idx + 1,
        id: p.product_id || null,
        title: p.title || null,
        keyword: keyword,
        country_code: '{country_code}',
        currency: currency,
        price: (currencySymbol && priceInfo.sale_price_format) ? (currencySymbol + priceInfo.sale_price_format) : (priceInfo.sale_price_format || null),
        min_price: salePrice,
        max_price: salePrice,
        origin_price: (currencySymbol && priceInfo.origin_price_format) ? (currencySymbol + priceInfo.origin_price_format) : (priceInfo.origin_price_format || null),
        discount_format: priceInfo.discount_format || null,
        product_rating: toNumber(rate.score),
        review_count: toNumber(rate.review_count),
        sold_count: toNumber(sold.sold_count),
        sold_count_str: sold.sold_count_str || (sold.sold_count != null ? String(sold.sold_count) : null),
        seller_id: seller.seller_id || null,
        seller_name: seller.shop_name || null,
        shop: {{
          shop_id: seller.seller_id || null,
          shop_name: seller.shop_name || null,
          shop_logo: pickUrls(seller.shop_logo)
        }},
        brand: brand.brand_name || null,
        images: pickUrls(p.image),
        transparent_images: pickUrls(p.transparent_image),
        product_url: seo.canonical_url || null,
        slug: seo.slug || null,
        skus: skus
      }};
    }});

    return JSON.stringify({{
      keyword: keyword,
      country_code: '{country_code}',
      count: items.length,
      has_more: !!cd.has_more,
      load_more_params: cd.load_more_params || null,
      products: items
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: 'Unhandled exception: ' + (e && e.message ? e.message : String(e)) }});
  }}
}})()
"""
    print(js)


if __name__ == '__main__':
    main()
