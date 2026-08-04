# TikTok Shop

Generated from SocQ Capability Registry schema `v1-dc091b011267`. Read this file when the request targets TikTok Shop.

## Endpoint selection

| Endpoint | Use for | Input choice | Cost |
| --- | --- | --- | --- |
| [`tiktok-shop/product`](https://docs.socq.ai/api-manual/tiktok-shop/product) | TikTok Shop Product API | url | 0.7 credits/result |
| [`tiktok-shop/product-reviews`](https://docs.socq.ai/api-manual/tiktok-shop/product-reviews) | TikTok Shop Product Reviews API | url | 0.3 credits/result |
| [`tiktok-shop/products`](https://docs.socq.ai/api-manual/tiktok-shop/products) | TikTok Shop Products API | url | 0.7 credits/result |
| [`tiktok-shop/search`](https://docs.socq.ai/api-manual/tiktok-shop/search) | TikTok Shop Search API | query | 0.7 credits/result |
| [`tiktok-shop/user-showcase`](https://docs.socq.ai/api-manual/tiktok-shop/user-showcase) | TikTok Shop User Showcase API | username | 0.7 credits/result |

## Validated examples

### `tiktok-shop/product`

Typed MCP tool: `socq_tiktok_shop_product`

```json
{
  "url": "https://www.tiktok.com/shop/pdp/example-product/1234567890123456789"
}
```

### `tiktok-shop/product-reviews`

Typed MCP tool: `socq_tiktok_shop_product_reviews`

```json
{
  "url": "https://www.tiktok.com/shop/pdp/example-product/1234567890123456789"
}
```

### `tiktok-shop/products`

Typed MCP tool: `socq_tiktok_shop_products`

```json
{
  "url": "https://www.tiktok.com/shop/store/example-store/1234567890123456789"
}
```

### `tiktok-shop/search`

Typed MCP tool: `socq_tiktok_shop_search`

```json
{
  "query": "wireless earbuds"
}
```

### `tiktok-shop/user-showcase`

Typed MCP tool: `socq_tiktok_shop_user_showcase`

```json
{
  "username": "example_creator"
}
```
