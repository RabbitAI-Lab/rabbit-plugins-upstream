---
name: workspace-access-checklist
description: Combines compare workspace access lists with create an access review checklist.
version: 1.0.7
metadata:
  openclaw:
    skillKey: workspace-access-checklist
---

# Workspace Access Comparator and Access Review Checklist

Use this skill for routine collaboration operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Workspace Access Comparator

Tool: `compare_workspace_access`

Reads current and approved workspace access lists and prepares a concise difference set.

Input field: `sharing_acl_json`. Current and approved workspace membership lists.

Output field: `access_delta`.

## Operation 2: Access Review Checklist

Tool: `create_access_checklist`

Creates access review checklists from workspace membership differences for collaboration handoffs.

Input field: `access_delta`. Workspace membership differences prepared for collaboration follow-up.

Output field: `checklist_artifact`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
