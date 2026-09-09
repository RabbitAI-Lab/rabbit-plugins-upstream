# Getting started with the Viral Outliers API & MCP server

Follow these steps in order. Steps 0 and the pricing lookup need no account at all.

## Step 0: try it without an account
```
curl https://viraloutliers.com/api/v1/trending
curl https://viraloutliers.com/api/v1/pricing
```
Both are free and unauthenticated: a live sample of the outlier feed, and the machine-readable price list.

## Step 1: create a free account
Sign up at https://viraloutliers.com/sign-up. A free account is enough to buy credits and use the API; a subscription additionally includes monthly credits (Basic Plan 250, Pro Plan 750, Agency Plan 3.000).

## Step 2: create an API key
Go to https://viraloutliers.com/settings?tab=api-keys and create a key. It starts with so_live_ and is shown ONCE, so store it immediately. You can revoke and rotate keys on the same page.

## Step 3: add credits
On the same API Keys tab, buy a one-time pack (1.500 credits for $15, 4.200 credits for $39, 12.000 credits for $99) or subscribe for a monthly allowance. 1 credit = $0.01. Billing is prepaid with a hard stop at zero: no surprise bills, ever.

## Step 4: make your first REST call
```
curl -X POST https://viraloutliers.com/api/v1/search/content \
  -H "Authorization: Bearer so_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "home workout", "platforms": ["tiktok"], "minOutlierScore": 5}'
```
Every billable response includes X-Credits-Charged and X-Credits-Balance headers, so you can track spend per call.

## Step 5: connect an AI agent via MCP
```
claude mcp add --transport http viral-outliers https://viraloutliers.com/api/mcp \
  --header "Authorization: Bearer so_live_YOUR_KEY"
```
In Claude.ai or ChatGPT, add a custom connector with the URL https://viraloutliers.com/api/mcp and the same key. The server is listed on the official MCP registry as com.viraloutliers/viral-outliers.

In OpenClaw (key in the VIRAL_OUTLIERS_API_KEY environment variable):
```
openclaw mcp add viral-outliers --url https://viraloutliers.com/api/mcp --transport streamable-http --header "Authorization=Bearer ${VIRAL_OUTLIERS_API_KEY}"
```
In Hermes Agent, add to config.yaml:
```
mcp_servers:
  viral-outliers:
    url: "https://viraloutliers.com/api/mcp"
    headers:
      Authorization: "Bearer ${VIRAL_OUTLIERS_API_KEY}"
```
A ready-made agent skill for this workflow is discoverable at https://viraloutliers.com/.well-known/skills/index.json.

## Step 6: run async work (crawls, transcripts, remixes)
Async skills charge on queueing and return a jobRef. Poll GET /api/v1/jobs/{jobRef} (free) every 10-30 seconds; when completed, fetch the result (transcripts and visual analyses land on GET /api/v1/posts/{postId}). Failed jobs refund automatically.

## Step 7: go further
- Full skill table and per-skill docs: https://viraloutliers.com/docs
- OpenAPI spec: https://viraloutliers.com/openapi.json
- Machine-readable site summary: https://viraloutliers.com/llms.txt
- On insufficient_credits (HTTP 402): call create_topup_link (POST /api/v1/credits/topup, free) for a payment link to hand the account owner.
- Found a bug? report_issue (POST /api/v1/feedback) is free.