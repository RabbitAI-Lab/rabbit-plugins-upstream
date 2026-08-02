#!/usr/bin/env bash
# create-github-issue.sh — Open a GitHub issue documenting template changes
# Usage: ./create-github-issue.sh <owner/repo> <title> <body-file>
#
# Requires: curl, jq
# Env vars:
#   GITHUB_TOKEN — Personal access token with repo scope

set -euo pipefail

REPO="${1:?Usage: $0 <owner/repo> <title> <body-file>}"
TITLE="${2:?Missing issue title}"
BODY_FILE="${3:?Missing body file path}"

TOKEN="${GITHUB_TOKEN:?Set GITHUB_TOKEN}"

if [ ! -f "$BODY_FILE" ]; then
  echo "ERROR: Body file not found: $BODY_FILE" >&2; exit 1
fi

BODY_JSON=$(jq -Rs . < "$BODY_FILE")
TITLE_JSON=$(echo "$TITLE" | jq -Rs .)

RESP=$(curl -s -X POST "https://api.github.com/repos/${REPO}/issues" \
  -H "Authorization: token $TOKEN" \
  -H 'Accept: application/vnd.github+json' \
  -H 'Content-Type: application/json' \
  -d "{\"title\": ${TITLE_JSON}, \"body\": ${BODY_JSON}, \"labels\": [\"documentation\", \"i18n\"]}")

ISSUE_URL=$(echo "$RESP" | jq -r '.html_url // empty')

if [ -z "$ISSUE_URL" ]; then
  echo "ERROR: Failed to create issue: $RESP" >&2; exit 1
fi

echo "Issue created: $ISSUE_URL"
