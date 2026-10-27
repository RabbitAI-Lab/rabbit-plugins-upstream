---
name: highlevel-agency-mcp
version: 1.0.0
description: Automate GoHighLevel (GHL) funnel and website page layouts, client domain DNS & SSL onboarding, multi-step forms, workflow graphs, LeadShield contact form spam & B2B solicitation blockers, spam-shield IVRs, and sub-account snapshot diffs using HighLevel Agency & Builder MCP.
---

# HighLevel Agency & Builder MCP

Author: Daniel Hallman

Use the **HighLevel Agency & Builder MCP** (`https://ghlagencymcp.com/mcp`) whenever the user wants to inspect, build, update, or verify GoHighLevel (GHL) funnels, websites, domains, forms, workflows, LeadShield contact form spam guards, call-screening IVRs, or sub-account snapshots.

## Quick start

1. Open [HighLevel Agency & Builder MCP](https://ghlagencymcp.com) for interactive blueprints, setup guides, or to connect your AI assistant to `https://ghlagencymcp.com/mcp`.
2. Connect any Streamable HTTP MCP client (`https://ghlagencymcp.com/mcp`) or install the public plugin repository from [github.com/mooshee/highlevel-agency-mcp](https://github.com/mooshee/highlevel-agency-mcp).

## Core Capabilities (13 Live MCP Tools)

1. **Connection Health, Account Discovery & Progressive Tool Packs (`ghl_agency_connection_health`, `ghl_agency_contexts`, `ghl_agency_doctor`, `ghl_agency_locations`, `ghl_agency_tools_search`, `ghl_agency_tools_enable`)**:
   - Check connection health, active Safe-Writes Policy preset, and progressive discovery status (`ghl_agency_connection_health`).
   - List configured agency account contexts (`ghl_agency_contexts`), verify Private Integration Token (PIT) and location readiness (`ghl_agency_doctor`), and inspect or update sub-account locations (`ghl_agency_locations`).
   - Search across all 55 domain operations (`ghl_agency_tools_search`) and dynamically enable specialized tool packs (`ghl_agency_tools_enable`) for the session.

2. **Funnel & Website Page Builder (`ghl_site_builder_sync`)**:
   - Export, inspect, diff, and update live funnel steps and website pages.
   - Modify headlines, copy, sections, and custom CSS while preserving native 2-step order forms, order bumps, and 1-click upsell blocks.
   - Sync page templates and layout revisions with local Git version control and dry-run diff previews before publishing.

3. **Client Domain, DNS & Branded Link Onboarding (`ghl_domain_ssl_onboard`)**:
   - Plan, verify, and attach funnel/website custom domains and branded short-link domains (`CNAME`, `A`, and `TXT` records).
   - Check DNS propagation, SPF/DKIM/DMARC, Apple Branded Mail logos, and SSL provisioning status before attaching domains.

4. **Workflows, LeadShield Form Spam Guards & Spam-Shield IVRs (`ghl_workflow_ivr_builder`)**:
   - Synthesize and publish multi-branch workflow automations from structured specifications, including 2-stage **LeadShield** contact form spam and B2B solicitation screening (`deliver_to_client` vs `spam_quarantine` branches with `$0.00` Stage 0 deterministic bot drops).
   - Provision call-screening IVR trees ("Press 1 to connect") on tracking numbers to block robocalls before forwarding to client phones.

5. **Snapshot Drift, Custom Values & Broken-Merge-Tag Auditing (`ghl_snapshot_diff_audit`, `ghl_custom_values_audit`)**:
   - Compare any live client sub-account against a reference Master Snapshot (`ghl_snapshot_diff_audit`) without overwriting live assets.
   - Batch-sync sub-account Custom Values and run the Broken-Merge-Tag & Placeholder Validator (`ghl_custom_values_audit`) across SMS/email templates to catch unresolved `{{ custom_values.* }}` references and `TBD`/`INSERT_HERE` placeholders before launch.

6. **Least-Privilege Role Governance & Telephony Wallet-Drain Audit (`ghl_user_role_governance`, `ghl_phone_wallet_audit`)**:
   - Provision staff and contractors using locked least-privilege presets (`va-support`, `sales-rep`, `client-admin`) that prevent accidental contact exports, or offboard sub-account access (`ghl_user_role_governance`).
   - Run read-only audits of LC Phone numbers and number pools (`ghl_phone_wallet_audit`) for unassigned numbers draining monthly balance, self-forwarding loops, and missing SMS/MMS capabilities.

## Safe Operating Principles

- **Explicit Context Selection**: Always confirm the target sub-account (`locationId`) and whether the operation targets a sandbox or production sub-account before mutating live assets.
- **Dry-Run, Read-Back & Safe-Writes Policy Presets**: Every write defaults to a read-only `--dry-run` preview and verifies persistence with a live read-back check. Supports Safe-Writes Policy Presets (`full-access`, `no-sending`, `no-deletes`, `read-only`) and Progressive Discovery (`--progressive`).

