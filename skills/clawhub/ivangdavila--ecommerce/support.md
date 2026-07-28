# Support — Service, Escalation and What to Compensate

Customer service in a store is mostly the same seven questions. The wins come from **removing the cause of the top question**, answering the rest fast with a consistent policy, and spending compensation where it retains a customer rather than where it silences one.

**Before answering a policy edge case or setting a compensation amount**, read `config.yaml` (`max_discount_pct`, `brand_and_policy`) and the policy artifacts `## Boxes` names. Improvised generosity is the reason two customers with the same problem get different answers and one of them posts about it.

## The Seven Questions and Their Real Fix

| Contact reason | Deflection that actually works |
|---|---|
| Where is my order? | Proactive dispatch and delay notifications, plus a tracking page on your own domain (`fulfillment.md`) |
| How do I return this? | Self-service portal linked from the delivery email, not an address in a policy page (`returns.md`) |
| Does it fit / will it work with X? | Sizing and compatibility data on the product page — the answer belongs in the catalog, not in a reply (`catalog.md`) |
| Can I change my address / order? | Self-service edit window before dispatch (`orders.md`) |
| My payment failed | In-session retry with an alternative method; the email version arrives too late (`payments.md`) |
| Where is my refund? | State the settlement time at refund and again on the day it settles |
| It arrived damaged / wrong | One-photo form that triggers the replacement immediately (`returns.md`) |

Track contacts per 100 orders. Above roughly 10, the store is paying salary for a fixable product or process defect; below 3, either the store is unusually clean or customers cannot find the contact route — check the second before celebrating the first.

## Response and Resolution Targets

Set by channel and by promise, then published. A target the customer does not know about cannot reassure them.

| Channel | First response | Resolution |
|---|---|---|
| Email / form | Same business day; within 4 business hours is a strong target | 24 business hours |
| Live chat | Under 2 minutes while staffed, with honest hours displayed | Same session for anything policy-driven |
| Phone | Under 60 seconds or a callback offer | Same call |
| Social / public review | Under 4 hours in public, then move to private | 24 hours |
| Marketplace messaging | Whatever the marketplace's metric requires — it is a suspension risk, not a courtesy (`marketplaces.md`) | Per marketplace |

Staffing arithmetic: `agents = (contacts per day × average handle time) ÷ (productive minutes per agent per day)`. At 120 contacts/day, 6 minutes each and 330 productive minutes, that is 720 ÷ 330 ≈ **2.2 agents** — before peak, absence and training. Peak multiplies contacts faster than orders, typically because delivery anxiety rises (`peak.md`).

## Escalation Triggers

Escalate to a human decision-maker immediately when any of these appear, regardless of order value:

- The words **chargeback, lawyer, consumer authority, complaint to the regulator**, or a formal legal notice
- A safety issue, injury claim, or a product defect that could affect other units — this becomes a recall question, not a support ticket
- Third contact on the same issue, or any thread longer than four exchanges
- A public post while the ticket is open
- Suspected fraud in either direction (`fraud.md`)
- A refund requested outside the published window above the auto-approve threshold
- Anything a policy does not cover — write the answer down afterwards so the second occurrence is not another escalation

## The Compensation Ladder

Compensation is a margin decision. The cap is `max_discount_pct` unless the customer's lifetime contribution justifies more, and the rule is: **fix first, compensate second, never compensate instead of fixing.**

| Situation | Default remedy |
|---|---|
| Late by 1-2 days, our fault | Apology with the new date; no compensation — money offered here trains complaints |
| Late by 3+ days, our fault | Refund the shipping paid |
| Carrier delay outside our control, customer still waiting | Shipping refund if they paid, and a reship or refund once the trace fails |
| Wrong item sent | Correct item shipped immediately, prepaid return, and a gesture within the cap |
| Damaged in transit | Immediate replacement or full refund at the customer's choice; carrier claim runs in parallel (`fulfillment.md`) |
| Out of stock after the order | Full refund the same day, plus a gesture — this is the failure customers forgive least |
| Priced wrong on the site | Honour it if the loss is small and the volume is contained; otherwise cancel, refund and explain in the same message before they discover it |
| Repeated failure to the same customer | Escalate; a third failure is a retention problem, not a service ticket (`retention.md`) |

Cost of retention vs acquisition is the arithmetic behind the ladder: comparing the gesture to CAC (`## Metrics`) turns "how much do we give" into a number rather than a mood.

## Writing Replies

- **One reply, three parts**: what happened, what you are doing about it, and by when — with a date, not "as soon as possible".
- Never ask the customer to repeat information already in the order. Every "can you confirm your order number" on a ticket that already has it is a satisfaction point spent for nothing.
- Templates cover the seven questions; every template has an obvious escape into a real answer. A store recognisable by its canned replies has automated its way into worse retention.
- Public reviews and complaints: answer in public, briefly and factually, then resolve in private. Never argue the facts publicly, and never offer compensation publicly — that becomes the new floor for everyone reading (`retention.md`).
- Tone follows `brand_and_policy` in `config.yaml`; the default is plain, specific and unapologetically direct about what went wrong.

## Automation Without Damage

- Automate **status**, not **judgement**: order lookups, tracking, return authorization inside policy, and refund status are safe; condition assessments, goodwill decisions and anything with a legal word in it are not.
- Every automated flow states how to reach a human in one step. Hidden escalation is the fastest way to turn a ticket into a chargeback.
- Macro quality decays: review the top ten macros quarterly against the policies they quote, or they will keep promising a window the store changed six months ago (`## Due`).
- Support data is customer data: aggregate counts and reason codes may be stored, transcripts and identities may not (SKILL.md Rule 9).

**Write after support work**: contacts per 100 orders and the dominant reason into `## Metrics` or `## Pain Points`, with what was changed to remove the cause; a systemic failure into `incidents/<year>.md`; the macro review cadence into `## Due`; and the compensation ladder, escalation rules and reply templates the store settles on into `artifacts/policy-support.md` with its `## Boxes` line (`memory-template.md`).
