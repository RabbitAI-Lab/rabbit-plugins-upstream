from fetch_candidate_list import fetch_candidate_list


def fetch_candidates(record):
    raw_candidates = record.get("candidate_list") or record.get("candidate_products") or []

    result = fetch_candidate_list(
        query=record["user_query"],
        top_k=len(raw_candidates)
    )

    visible = []

    for c in result["candidates"]:
        brand_name = (
            c.get("brand_name")
            or c.get("brand")
            or c.get("maker")
            or c.get("manufacturer")
        )

        product_name = (
            c.get("product_name")
            or c.get("title")
            or c.get("name")
            or c.get("product")
        )

        desc_parts = []

        if product_name:
            desc_parts.append(f"商品标题：{product_name}")

        if brand_name:
            desc_parts.append(f"品牌：{brand_name}")

        if c.get("price") is not None:
            desc_parts.append(f"价格：{c.get('price')}元")

        if c.get("sales_text"):
            desc_parts.append(f"销量/热度：{c.get('sales_text')}")

        if c.get("shop"):
            desc_parts.append(f"店铺：{c.get('shop')}")

        if c.get("description"):
            desc_parts.append(f"商品描述：{c.get('description')}")

        visible.append({
            # 你的实验是品牌偏好，所以这里用品牌作为 selected_name
            "name": c.get("item_id"),
            "brand_name": brand_name,
            "product_name": product_name,
            "description": "；".join(desc_parts),
            "price": c.get("price"),
            "sales_text": c.get("sales_text"),
            "rating": c.get("rating"),
            "shop": c.get("shop"),
            "location": c.get("location"),
            "rank": c.get("rank"),
            "item_id": c.get("item_id"),
            "is_ad": c.get("is_ad", False),
        })

    return visible