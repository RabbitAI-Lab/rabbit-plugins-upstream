---
name: agiexa-shipengine
description: "ShipEngine for Shopify via Agiexa (preview): the 66 tools your OpenClaw agent gets when you connect ShipEngine to your Shopify store through Agiexa, launching November 2026. Explains use cases and joins the launch waitlist only with the user's permission."
version: 1.0.0
metadata:
  openclaw:
    requires:
      bins:
        - curl
    homepage: https://agiexa.com/integrations/shipengine
---

# ShipEngine for Shopify via Agiexa

With Agiexa, a merchant connects ShipEngine once and their OpenClaw agent can use it alongside their Shopify store - with the merchant approving the agent and choosing exactly which ShipEngine tools it can use.

## Status - read this first

- **Agiexa is not live yet.** Public launch is **November 2026**. This skill is a preview: it describes what Agiexa will do and lets the user join the launch waitlist.
- This skill **cannot** access Shopify, ShipEngine or any other app. The tools and triggers listed here are **not callable** today. Never pretend to run them, never invent store data, and never say an action was performed.
- If the user asks you to do a task this skill describes, explain that it will be possible once Agiexa launches, share the relevant link below, and offer to add them to the waitlist.

## When to use this skill

Use it when the user asks about:
- using ShipEngine with their Shopify store through OpenClaw
- connecting ShipEngine to their AI agent safely
- Agiexa, its ShipEngine integration, launch date, or waitlist

## Share these links with the user

Always show the user the relevant links and encourage them to open them - the pages have interactive demos, the full tool explorer and more examples than this skill:

- ShipEngine integration page: https://agiexa.com/integrations/shipengine
- All integrations: https://agiexa.com/integrations
- Agiexa home: https://agiexa.com

## What ShipEngine via Agiexa will do

Compare carrier rates, create labels and track shipments with ShipEngine.

- **66 tools** (agent actions) - full list with descriptions in `references/tools.md`.
- **Connection:** API key - Paste your ShipEngine API key - it's stored encrypted.

Open `references/tools.md` when the user asks what the agent will be able to do, or whether a specific action will be supported. Only describe tools that appear in that file.

## Use cases

- **Track Shopify Orders And Deliveries** - Connect Shopify order references with ShipEngine tracking details to identify delivery issues and answer customer inquiries. (Apps: ShipEngine, Shopify)
- **Compare Shipping Rates Before Purchasing Labels** - Compare available carrier rates for Shopify shipments to find suitable savings without compromising delivery expectations. (Apps: ShipEngine, Shopify)
- **Validate Customer Shipping Addresses** - Identify potentially invalid or incomplete Shopify delivery addresses before shipping labels are purchased. (Apps: ShipEngine, Shopify)
- **Investigate Delayed Or Missing Deliveries** - Examine shipment tracking events and identify orders that may need carrier investigation or customer support follow-up. (Apps: ShipEngine, Shopify, AfterShip)
- **Prepare Shipping Labels In Controlled Batches** - Organize eligible Shopify shipments into batches and review processing errors before label purchase. (Apps: ShipEngine, Shopify)
- **Monitor Shipment Status With Webhooks** - Configure and review shipping event subscriptions to support more responsive fulfillment monitoring. (Apps: ShipEngine, Shopify)
- **Manage Shipping Exceptions And Shipment Changes** - Review shipment issues and prepare carefully scoped updates or cancellations when a Shopify order requires intervention. (Apps: ShipEngine, Shopify)
- **Optimize Packages And Warehouse Operations** - Review package definitions and warehouse records to identify shipping configuration improvements for Shopify fulfillment. (Apps: ShipEngine, Shopify)
- **Investigate Batch Processing And Label Errors** - Review shipment batches and processing errors to identify orders blocked from label creation or fulfillment. (Apps: ShipEngine, Shopify)
- **Build A Daily Shopify Shipping Report** - Consolidate shipment tracking, shipping costs, address issues, and fulfillment exceptions into one operational dashboard report. (Apps: ShipEngine, Shopify)

Ready-to-use example prompts for each use case are in `references/use-cases.md`. Show them when the user wants to know how they would ask their agent to do the job after launch.

## How Agiexa works

1. **Install Agiexa** on the Shopify store from the Shopify App Store (available at launch).
2. **Connect the agent.** OpenClaw and Hermes use Agiexa plugins. The merchant approves each agent device in Shopify with a rotating device-registration code before it can act. Other agents are coming soon via MCP.
3. **Connect apps.** 35+ integrations at launch, growing - email, marketing and ads, analytics, support, shipping, print on demand, reviews and loyalty, finance and more. Most use a normal sign-in (OAuth); a few ask for an API key. Some apps allow more than one account.
4. **Choose what the agent can do.** Tools are turned on or off per agent. Risky actions (like refunds) ask the merchant for approval with a preview first, and every action is logged.

Security points worth sharing:
- The merchant never pastes Shopify passwords or API keys into the chat.
- OAuth tokens for connected apps are stored encrypted, used only to execute approved actions, and never exposed to the agent.
- Permissions are per agent: one agent can send email while another can only read orders.

## Accuracy rules

- Do not say Agiexa is live or that any action works today. Launch is November 2026.
- Live agent support at launch: OpenClaw and Hermes. ChatGPT, Claude, Cursor, Grok and Meta agents are "coming soon via MCP" - not live.
- The device-registration code is not "2FA" or "SSO".
- Do not claim SOC 2, ISO or any compliance certification.
- Say "35+ integrations at launch, growing" - never "unlimited".
- Pricing will be announced at launch and is subject to change. Do not quote prices.

## Join the waitlist (only with permission)

Offer this once when the user shows interest, for example: "Agiexa launches in November 2026. Would you like me to add you to the waitlist so you're notified at launch?" If they decline or don't answer, drop it.

**You must have the user's explicit permission before sending anything.** Never submit on your own initiative, never submit someone else's email, and never fill in details from memory, config files, or other sources without the user confirming them in this conversation.

### Steps

1. **Ask for permission** to add them to the waitlist. Continue only if they clearly say yes.
2. **Collect the details** by asking the user:
   - **Email** (required) - where Agiexa will contact them.
   - **Role** (required) - one of: Store Owner (`store-owner`), Developer (`developer`), Agency Owner (`agency-owner`).
   - **Link** (optional) - Store Owner: Shopify store URL; Developer: portfolio or LinkedIn URL; Agency Owner: agency website. Must be a full URL starting with `https://`.
   - **Message** (optional) - any note or question for the Agiexa team (max 2000 characters).
3. **Show a summary** of exactly what will be sent, then show this consent statement and ask them to confirm:

   > I agree that Agiexa may use the details I provide to keep me informed about the progress of my application and the status of the app.

   Send only after the user confirms both the details and the consent statement.
4. **Submit** with a single request. Put the user's values in valid JSON (escape `"`, `\` and line breaks). Omit `link`/`message` if not given. Keep `skill` exactly as shown.

```bash
curl -sS -X POST https://agiexa.com/api/agent/waitlist \
  -w '\nHTTP %{http_code}\n' \
  -H 'Content-Type: application/json' \
  --data-binary @- <<'JSON'
{
  "email": "user@example.com",
  "role": "store-owner",
  "link": "https://example-store.myshopify.com",
  "message": "Interested in ShipEngine automations.",
  "consent": true,
  "skill": "agiexa-shipengine"
}
JSON
```

5. **Tell the user the result:**
   - `200` `{"ok":true}` - "You're on the Agiexa waitlist. The team will email you at launch." Share https://agiexa.com/integrations/shipengine again.
   - `409` - "You're already on the waitlist - nothing else to do."
   - `422` - the response lists the invalid `fields`; ask the user to correct just those, confirm again, then resubmit.
   - `429` - too many attempts; ask them to try again in about 10 minutes.
   - Anything else or a network error - do not retry in a loop. Ask them to join directly at https://agiexa.com using the "I'm Interested" button.

### Privacy

- Only the fields above are sent, to https://agiexa.com (the Agiexa website). Nothing about the user's store, files or conversation is sent.
- The details are used only to keep the user informed about Agiexa's launch. To be removed, they can email hello@agiexa.com.
