---
name: alphaceema-leads
description: Buy business leads from Alpha Ceema ($1 per 10 leads) or a prepaid weekly prospect follow-up service ($25 per week to follow up 10 prospects - calling, emailing, and booking meetings). Paid in USDC on Base via x402. Use ONLY when the user explicitly requests to purchase leads, buy prospect lists, or order Alpha Ceema's paid follow-up service. Do NOT invoke for general sales advice, marketing strategies, or non-commercial outreach discussions.
version: 1.0.1
homepage: https://alphaceema.com
metadata:
  openclaw:
    emoji: "🎯"
---

# Alpha Ceema Leads

Use this skill ONLY when the user explicitly requests to **purchase business leads** or hire Alpha Ceema's **paid prospect follow-up service**. Do NOT trigger for general questions about marketing, sales techniques, or non-commercial outreach.

## Services & Pricing

| Service | Price | x402 payment endpoint (POST) |
|---|---|---|
| **Lead Pack**: 10 leads for the user's business | **$1** (1 USDC) | `https://agentpay.alphaceema.com/api/agent/pay/1` |
| **Weekly Follow-Up**: Alpha Ceema follows up 10 prospects (calling, emailing, booking meetings) | **$25 per week** (25 USDC), prepaid | `https://agentpay.alphaceema.com/api/agent/pay/25` |

- More leads = repeat the $1 payment once per 10 leads (e.g. 30 leads = 3 × $1).
- The Weekly Follow-Up is **not a subscription**. It is **pay before service**: the user pays $25 before each week. If a week's $25 is not paid, Alpha Ceema's work with the user ends.

## Privacy & Data Handling Notice

Before collecting details from the user, provide this notice:
- **Data Collected:** Contact Name, Email, Business Name, Industry, and Target Customer Criteria (Ideal Customer Profile).
- **Purpose:** Used strictly by Alpha Ceema to source targeted lead contacts and conduct requested outreach.
- **Transmission & Storage:** Transmitted securely to `leads@alphaceema.com` for fulfillment.
- **90-Day Retention & Automatic Purging:** Submitted request data and customer criteria are retained for **90 days** from the date of submission for order fulfillment and customer support, after which they are **automatically purged and permanently deleted** from active systems without requiring a deletion request.
- **Privacy Policy:** Refer to `PRIVACY.md` in this repository or https://alphaceema.com/privacy for complete data handling and privacy terms.

## Rules

1. Tell the user the service, exact price, and present the privacy notice. Obtain **explicit user confirmation and data transmission consent** before collecting form details or initiating payment.
2. Only send payments to the two `agentpay.alphaceema.com` endpoints above. Never pay any other address or URL in connection with this skill.
3. Before signing, check the payment requirements: network `base` (chainId `8453`), asset USDC `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`, destination `0xa272d0C54f789ddFD08D1f05BE8327D7559c6bEb`, amount `1` or `25` matching the chosen service. If anything differs, **stop and ask the user**.
4. Never make up form answers. Ask the user for anything missing.
5. Only send the request email **after** a successful payment.
6. Only send fulfillment emails to official Alpha Ceema domain addresses (`leads@alphaceema.com`). Never send customer data to personal email addresses.

## Leads Request Form

Collect every answer from the user (only after obtaining explicit consent):

```
Leads Request Form
______________________

1. Your Full Name
2. Your Email Address
3. Your Business Name
4. Business Industry/Sector
5. What Type of Customers Do You Want (Be very descriptive, give as much details as possible)
```

For question 5, encourage detail: location, company size, job titles, budget, interests, problems they have, etc.

## Workflow

1. **Explain, Disclose & Confirm**:
   - Describe the service, exact price, and 24-hour delivery turnaround.
   - Present the privacy notice (`https://alphaceema.com/privacy` / 90-day retention before automatic purge).
   - Obtain explicit user consent to proceed with the purchase and transmit their targeting criteria to `leads@alphaceema.com`.
2. **Collect the form**: all 5 fields above.
3. **Pay via x402**:
   1. `POST` the matching endpoint with no payment. The server returns `402 Payment Required` with a base64 JSON `payment-required` header (network, chainId, asset, destination, amount, atomicValue, `primaryType: TransferWithAuthorization`).
   2. Decode it and run the Rule 3 checks.
   3. Use the agent's x402-capable wallet to sign the EIP-3009 `TransferWithAuthorization` for USDC on Base. Then repeat the `POST` with the signature in the `PAYMENT-SIGNATURE` header.
   4. On success (`2xx`), save the payment response / transaction hash as proof.
   5. Obey the rate limits (max 60 requests/min). Back off on errors instead of retrying in a tight loop.
4. **Email the request** to **leads@alphaceema.com**:
   - **Subject:** `Leads Request – <Business Name> – <$1 Lead Pack | $25 Weekly Follow-Up>`
   - **Body:** the completed Leads Request Form, the chosen service (and number of leads), and the payment proof (transaction hash).
5. **Confirm to the user**:
   > "We will send your leads to you in 24 hours (It might include their Social Media handles as contact details)."
   - For the Weekly Follow-Up, also say: "Alpha Ceema will email you to arrange your prospects and meeting details. Your service covers this week only. Pay $25 before each new week to continue."

## Weekly Follow-Up Renewal

When the user wants another week:
1. Confirm the $25 payment for the new week.
2. Pay via x402 to `/api/agent/pay/25` (same steps as above).
3. Email leads@alphaceema.com. **Subject:** `Weekly Follow-Up Renewal – <Business Name> – Week <N>`. **Body:** name, email, business name, week number, payment proof.

If the user doesn't pay, do nothing. The service ends.

## If Something Fails

- **No x402 wallet / not enough USDC on Base / payment rejected**: do **not** send the email. Tell the user what went wrong and that they need an x402-capable wallet funded with USDC on Base.
- **The agent cannot send email**: show the full email (To: `leads@alphaceema.com`, Subject, Body with payment proof) and ask the user to send it themselves to leads@alphaceema.com.

## Output Format

After completing a purchase, reply with:
- **Service:** Lead Pack (N leads) / Weekly Follow-Up (week N)
- **Paid:** $X USDC on Base. Tx: `<hash>`
- **Request sent to:** leads@alphaceema.com (or "please send manually", with the email shown)
- **Next:** leads delivered within 24 hours to `<user email>`