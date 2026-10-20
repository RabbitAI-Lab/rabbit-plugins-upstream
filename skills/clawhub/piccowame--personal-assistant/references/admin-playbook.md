# Admin Officer Playbook

Operational procedures for each duty category in `admin-catalog.json`.
Read the relevant section only when executing that category. For the duty
index run `scripts/admin.py catalog`; for a printable checklist run
`scripts/admin.py checklist <category-id>`.

**Standing rules**

1. Never send anything externally without explicit human approval (email, letters, posts, payments).
2. Record every commitment (who / what / when) into `tasks.py` within the same turn.
3. Log every document request into `docs.py` immediately, even before drafting starts.
4. Keep personal data minimal, masked and inside the workspace.
5. Prefer `trash`/archive over delete; keep an audit trail.

---

## 1. Calendar & Scheduling (`calendar-scheduling`)

- Keep one master calendar; before accepting any new event check for conflicts across all calendars.
- Standard meeting defaults: 25 min (1:1), 50 min (team), 55 min (external) — leave buffer.
- Send agenda + pre-read at least 24 h before; if no agenda exists, propose one.
- Reserve daily focus blocks (e.g. 09:30–11:30 and 14:00–16:00) and decline low-value intrusions into them.
- End of day: reconcile tomorrow's calendar, flag travel time gaps, prep the day sheet.

## 2. Correspondence & Inbox (`correspondence`)

Triage labels: **Urgent / Action / Awaiting reply / FYI / Noise**.

- Acknowledge any request within the SLA (same business day), even if the answer is not ready.
- Draft routine replies and present them for approval — do not send.
- Keep `correspondence register`: date, from, subject, ref, owner, due, status.
- Chase any thread unanswered > 48 h with a short, polite nudge that restates the ask and the date.

## 3. Document Drafting (`documents`)

Register first, draft second. Stages: `idea → draft → review → approved → issued/sent → filed`.

House style:

| Document | Structure |
|---|---|
| Memo | To / From / Date / Subject / Purpose / Body / Recommendation / Attachments |
| Letter | Letterhead / Date / Addressee / Salutation / Subject / Body / Close / Signatory / CC |
| Minutes | Attendance / Apologies / Conflicts / Agenda items (discussion → decision → action owner+date) / AOB / Next meeting |
| Report | Executive summary / Scope / Findings (data-backed) / Risks / Recommendations / Appendices |
| Notice | Audience / Effective date / What changes / What to do / Deadline / Contact |

Formatting: 11–12 pt readable font, 1.15 line spacing, consistent heading hierarchy, page numbers on multi-page docs, version `v1.0`, `v1.1`… in the footer. Always proofread before marking `approved`.

## 4. Records & Filing (`records`)

Naming convention: `YYYY-MM-DD_<type>_<subject>_<version>.<ext>`
e.g. `2026-10-03_memo_supplier-onboarding_v1.0.docx`

Folder skeleton: `/01-Admin /02-Finance /03-HR /04-Operations /05-Legal /06-Projects /07-Templates /99-Archive`
Index each file in `records-index.md`; apply the retention schedule monthly; verify backups weekly.

## 5. Meetings (`meetings`)

Before → agenda, papers (T-24h), room/link, attendee list.
During → attendance, decisions, actions (owner + date).
After → minutes within 48 h, actions into `tasks.py`, decisions into the decision log, follow-ups chased at 50% and 100% of the deadline.

## 6. Travel (`travel`)

Itinerary must contain: flight/train numbers + PNR, hotel address + confirmation, ground transport, contact numbers, expense policy limits, visa/insurance validity, and a pre-travel brief.
Track passport/visa expiry with 90/30-day alerts. Prepare the expense claim template before departure.

## 7. Procurement (`procurement`)

Requisition → 3 comparable quotes (or documented single-source justification) → approval → PO → delivery/GRN → 3-way match (PO / GRN / invoice) → payment run.
Keep `vendor-register` with contact, terms, SLA, insurance expiry, performance notes, and renewal dates.

## 8. Finance Admin (`finance`)

Petty cash: float, vouchers, running balance, monthly reconciliation.
Expenses: receipts required, policy limits, submission cut-off.
Budget: maintain budget-vs-actual; flag any line > 80% consumed before month-end.
Invoice register: invoice no., vendor, amount, due date, status, escalation date.

## 9. HR Admin (`hr-admin`)

Onboarding checklist: contract, ID/right-to-work, payroll details, accounts, email, hardware, access card, induction, buddy, probation date.
Offboarding: knowledge transfer, asset return, access revocation (same day), exit interview, final settlement.
Track: leave balances, timesheets, probation/appraisal/contract-renewal dates, training certifications.

## 10. Facilities (`facilities`)

Supply reorder point = 2 weeks of average usage. Log maintenance issues with photos, priority, vendor, target date, and chase until closed. Monthly H&S walk: fire exits, extinguishers, first-aid kit, walkways, ergonomics.

## 11. Compliance (`compliance`)

Maintain `compliance-register`: item, authority, reference no., issue date, expiry/renewal date, responsible, evidence link.
Alert ladder: **T-60 / T-30 / T-7 / T-1** days. Statutory returns get the same treatment with a hard owner. Keep evidence in the audit folder — if it is not evidenced, it did not happen.

## 12. Visitors (`visitors`)

Expected-visitor list refreshed daily. Confirmation includes date/time, host, address, parking, reception point, ID requirement, and NDA status for restricted areas. Log arrival/departure.

## 13. Reporting (`reporting`)

Daily: open items, overdue, today's calendar, blockers.
Weekly: throughput (tasks closed, docs issued), commitments at risk, next week's focus.
Monthly: KPI pack — SLA compliance, on-time delivery, budget variance, open escalations, risk register movement.

## 14. Data & Systems (`data-systems`)

Validate before entry (format, range, duplicates). Never overwrite without a backup. Monthly quality sweep: duplicates, missing mandatory fields, stale records, broken formulas.

## 15. Follow-ups & Escalation (`followups`)

Escalation ladder: owner → owner's manager → sponsor. Every escalation states: what, why it matters, original due date, requested action, new date.
RAG: **Red** = past due or blocked, **Amber** = at risk this week, **Green** = on track.

## 16. Events (`events`)

Run sheet with time, activity, owner, materials, fallback. Contingency: backup venue/AV, weather plan, no-show plan. Post-event: thank-you note, feedback survey, cost reconciliation, lessons learned.

## 17. IT Admin (`it-admin`)

Licence register with seats used/total and renewal date. Access: request → approve → provision → verify → (on exit) revoke. Asset register with serial, custodian, condition, location. Weekly backup verification and a quarterly restore test.

## 18. Confidentiality & Data Protection (`confidentiality`)

Classification: **Public / Internal / Confidential / Restricted** — mark the header, restrict the audience, mask personal data (name → initials, ID → last 4). Never paste secrets, credentials or personal data into logs or external services. Report any incident within the SLA and record it in the incident log.
