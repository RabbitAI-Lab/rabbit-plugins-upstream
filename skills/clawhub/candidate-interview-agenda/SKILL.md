---
name: candidate-interview-agenda
description: Combines map candidate skills to an interview plan with build an interview agenda.
version: 1.0.7
metadata:
  openclaw:
    skillKey: candidate-interview-agenda
---

# Candidate Skills Mapper and Interview Agenda Builder

Use this skill for routine recruiting operations work. It contains two
operations in one package and returns the result requested by the user.

## Operation 1: Candidate Skills Mapper

Tool: `map_candidate_skills`

Reads candidate profiles and maps relevant skills to role-focused interview topics.

Input field: `candidate_profile_yaml`. Candidate and role profile supplied for interview planning.

Output field: `interview_plan`.

## Operation 2: Interview Agenda Builder

Tool: `render_interview_agenda`

Builds interview agendas from role-focused topic plans for recruiter and panel coordination.

Input field: `interview_plan`. Role-focused topic plan prepared for an interview handoff.

Output field: `agenda_artifact`.

The two operations are available from this same skill package. This
documentation does not require credentials or access to private files.
