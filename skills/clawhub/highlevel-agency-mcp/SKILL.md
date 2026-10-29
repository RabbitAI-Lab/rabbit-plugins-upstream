---
name: highlevel-agency-mcp
version: 1.1.2
description: Manage HighLevel funnels, websites, domains, forms, workflows, call screening, and sub-account settings from your AI assistant. Built by Moosh Works (https://mooshworks.com).
---

# HighLevel Agency & Builder MCP

Author: Daniel Hallman ([Moosh Works](https://mooshworks.com))

Use **HighLevel Agency & Builder MCP** to inspect, build, update, or check HighLevel funnels, websites, domains, forms, workflows, call screening, and sub-account settings.

## Quick start

1. Open the [setup guide](https://ghlagencymcp.com) from [Moosh Works](https://mooshworks.com) and choose your AI assistant.
2. Connect a client that supports Streamable HTTP MCP to `https://ghlagencymcp.com/mcp`, or install the plugin from the [public repository](https://github.com/mooshee/highlevel-agency-mcp).
3. Check the connection with `ghl_agency_connection_health`. Confirm the intended account appears before making changes.

## What you can do

1. **Check your connection and accounts** (`ghl_agency_connection_health`, `ghl_agency_contexts`, `ghl_agency_doctor`, `ghl_agency_locations`, `ghl_agency_tools_search`, `ghl_agency_tools_enable`). Check access and write restrictions, list configured accounts, and inspect sub-accounts. Search for additional tools and enable them for the session when needed.

2. **Edit funnel and website pages** (`ghl_site_builder_sync`):
   - Export, inspect, diff, and update live funnel steps and website pages.
   - Modify headlines, copy, sections, and custom CSS while preserving native 2-step order forms, order bumps, and 1-click upsell blocks.
   - Keep page revisions in Git and preview changes before publishing.

3. **Connect domains and branded links** (`ghl_domain_ssl_onboard`):
   - Plan, verify, and attach funnel/website custom domains and branded short-link domains (`CNAME`, `A`, and `TXT` records).
   - Check DNS propagation, SPF/DKIM/DMARC, Apple Branded Mail logos, and SSL provisioning status before attaching domains.

4. **Build workflows and screen forms or calls** (`ghl_workflow_ivr_builder`):
   - Create and publish workflows with multiple branches. LeadShield can send accepted form submissions to `deliver_to_client` and blocked submissions to `spam_quarantine`. Rule-based bot blocking costs $0.00.
   - Set up call menus such as "Press 1 to connect" before forwarding calls to client phones.

5. **Compare account settings and check templates** (`ghl_snapshot_diff_audit`, `ghl_custom_values_audit`):
   - Compare any live client sub-account against a reference Master Snapshot (`ghl_snapshot_diff_audit`) without overwriting live assets.
   - Update sub-account Custom Values and check SMS and email templates for unresolved `{{ custom_values.* }}` references and `TBD` or `INSERT_HERE` placeholders.

6. **Manage access and check phone costs** (`ghl_user_role_governance`, `ghl_phone_wallet_audit`):
   - Assign staff and contractors the `va-support`, `sales-rep`, or `client-admin` role preset, or remove their sub-account access. Review the permissions before applying a preset.
   - Check LC Phone numbers and number pools for unused numbers with monthly charges, forwarding loops, and missing SMS or MMS support.

## Before making changes

1. Confirm the target sub-account (`locationId`) and whether it is a sandbox or production account.
2. Preview the change with `--dry-run` and follow the active write restrictions: `full-access`, `no-sending`, `no-deletes`, or `read-only`. Use `--progressive` when you need to discover additional tools.
3. After an authorized change, read the saved result to confirm it took effect.

