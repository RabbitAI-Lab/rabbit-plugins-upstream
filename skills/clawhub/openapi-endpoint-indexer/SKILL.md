---
name: openapi-endpoint-indexer
description: >
  Build a sorted index of paths and methods from an OpenAPI JSON document
  the user provides. Use when surveying an API surface area.
---

# OpenAPI Endpoint Indexer

## Purpose / Overview
Lists `METHOD path` lines sorted by path from OpenAPI 3 JSON.

## When to Use
API reviews; generating smoke-test checklists.

## Usage / Instructions
1. Accept OpenAPI JSON (paste or file path).
2. Walk `paths` → methods.
3. Print `GET /v1/foo` style lines; count totals by method.

## Examples
Small petstore-like spec → indexed method list.

## Requirements / Dependencies
None for pasted JSON; read file only if path given.

## Limitations / Caveats
Ignores webhooks/callbacks sections.

## Security / Permissions
Local read of user-provided content only. No live calls to the API.

## Attribution / License
MIT-0
