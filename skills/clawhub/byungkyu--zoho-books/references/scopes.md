# Zoho Books scopes

The OAuth scopes Zoho Books connections can ask for. Pass the ones the task needs with `--scopes` (repeatable or comma-separated) when creating the connection, or to `maton connection reauthorize` to change them later. *Always* scopes are added whatever you pass, *By default* ones are requested when you pass none, and *Optional* ones only when you pass them. Change them only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/zoho-books#permissions.

```bash
maton connection create zoho-books --scopes ZohoBooks.contacts.READ
```

| Scope | Requested |
| --- | --- |
| `ZohoBooks.contacts.ALL` | By default |
| `ZohoBooks.invoices.ALL` | By default |
| `ZohoBooks.customerpayments.ALL` | By default |
| `ZohoBooks.creditnotes.ALL` | By default |
| `ZohoBooks.expenses.ALL` | By default |
| `ZohoBooks.salesorders.ALL` | By default |
| `ZohoBooks.purchaseorders.ALL` | By default |
| `ZohoBooks.bills.ALL` | By default |
| `ZohoBooks.settings.ALL` | By default |
| `ZohoBooks.vendorpayments.ALL` | By default |
| `ZohoBooks.banking.ALL` | By default |
| `ZohoBooks.estimates.ALL` | By default |
| `ZohoBooks.debitnotes.ALL` | By default |
| `ZohoBooks.contacts.READ` | Optional |
| `ZohoBooks.invoices.READ` | Optional |
| `ZohoBooks.customerpayments.READ` | Optional |
| `ZohoBooks.creditnotes.READ` | Optional |
| `ZohoBooks.expenses.READ` | Optional |
| `ZohoBooks.salesorders.READ` | Optional |
| `ZohoBooks.purchaseorders.READ` | Optional |
| `ZohoBooks.bills.READ` | Optional |
| `ZohoBooks.settings.READ` | Optional |
| `ZohoBooks.vendorpayments.READ` | Optional |
| `ZohoBooks.banking.READ` | Optional |
| `ZohoBooks.estimates.READ` | Optional |
| `ZohoBooks.debitnotes.READ` | Optional |
| `AaaServer.profile.READ` | Always |
