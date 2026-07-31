# Changelog

All notable changes to the Odoo Connector skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.1] — 2026-07-30

### Security & Compliance
- **Refined CAPTCHA section language** — replaced "bypass" terminology with "handling CAPTCHA challenges" to comply with security audit requirements
- **Added Legal & ToS Notice** — explicit warning about authorization requirements and Terms of Service compliance for CAPTCHA automation
- **Added write-operation warnings** — Create/Update/Delete sections now include warnings about live system impact and staging-first recommendation
- **Added state-changing action warnings** — Examples using `action_confirm` and similar methods now warn about downstream workflow triggers (fulfillment, invoicing, notifications)
- **Fixed hardcoded secret in SECURITY.md** — replaced example password with clear placeholder to avoid exposed_secret_literal detection
- **Added Legal & ToS Compliance section** in SECURITY.md — authorization requirements, ToS guidance, account lockout risk, responsible use policy
- **Expanded Security Checklist** — added authorization, ToS compliance, and staging test items

## [1.2.0] — 2026-07-26

### Changed
- **Added `related_skills` in YAML frontmatter** — declares `camofox-default-browser` as recommended anti-detection browser for bypassing CAPTCHA/Cloudflare during Odoo web UI login
- **Step 1 now includes CAPTCHA troubleshooting block** — explains that production Odoo instances often block automated login; recommends camofox-default-browser skill, with fallback suggestions (different IP, VPN off, uBlock Origin)
- Clarified that self-hosted/local Odoo instances don't need CAPTCHA handling

## [1.1.0] — 2026-07-26

### Changed
- **Authentication Setup promoted to prominent first-time section** — Added "⚡ FIRST TIME? START HERE" section with clear decision flow for AI agents encountering a new Odoo instance
- Added explicit instruction: **no API key → login to web UI first → generate API key → then proceed to XML-RPC**
- Added decision flow diagram (YES/NO tree)
- Added "What You Need Before Coding" table with clear sources for each credential
- Added troubleshooting tip for missing API Keys section (Developer Mode hint)
- Added Step 3: Verify Credentials code snippet before proceeding to CRUD operations
- Clarified that API key generation is REQUIRED, not optional

## [1.0.0] — 2026-07-24

### Added

- Initial release of the Odoo Connector skill for OpenClaw
- Full XML-RPC API integration for Odoo 17, 18, and 19
- Authentication via Common endpoint (database + username/password/API key)
- CRUD operations on all Odoo models (`search`, `read`, `create`, `write`, `unlink`)
- Combined `search_read` operation for efficient data retrieval
- Domain filter support with all comparison operators (`=`, `!=`, `>`, `<`, `in`, `ilike`, etc.)
- Logical operators (`&`, `|`, `!`) for complex query construction
- Field discovery via `fields_get` method
- Support for all record pagination parameters (`limit`, `offset`, `order`)
- Comprehensive documentation:
  - Installation guide with prerequisites and environment setup
  - Quick start tutorial with step-by-step examples
  - Full API reference covering all supported models (50+ models documented)
  - Troubleshooting guide with common errors and solutions
- Example workflows:
  - Sales order creation (quotation → line items → confirmation)
  - Inventory synchronization (stock quants → aggregation → reporting)
- Utility scripts:
  - `test-connection.py` — verify Odoo connectivity and authentication
  - `bulk-import.py` — CSV-based bulk record creation with validation
- Security documentation and best practices
- Contributing guidelines

### Supported Models

- **Core:** `res.partner`, `res.users`, `res.company`
- **Products:** `product.product`, `product.template`, `product.category`
- **Sales:** `sale.order`, `sale.order.line`
- **Purchase:** `purchase.order`, `purchase.order.line`
- **Inventory:** `stock.picking`, `stock.move`, `stock.quant`, `stock.location`
- **Accounting:** `account.move`, `account.payment`, `account.journal`
- **CRM:** `crm.lead`, `crm.opportunity`
- **HR:** `hr.employee`, `hr.contract`, `hr.department`
- **Projects:** `project.project`, `project.task`, `project.tags`
- **Manufacturing:** `mrp.production`, `mrp.bom`, `mrp.workorder`

## [Unreleased]

### Planned

- WebSocket support for real-time Odoo notifications
- Batch operations API (multiple records in single call)
- Report generation via XML-RPC
- Attachment/file upload support
- Multi-database switching in a single session
- Interactive field explorer for unknown models
