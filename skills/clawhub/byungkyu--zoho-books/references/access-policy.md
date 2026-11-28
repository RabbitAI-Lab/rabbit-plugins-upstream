# Zoho Books access policy

An access policy limits which endpoints Zoho Books connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/zoho-books#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Zoho Books: its 147 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create zoho-books --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "books/v3/bankaccounts"},
    {"method": "GET", "path": "books/v3/bankaccounts/{id}"},
    {"method": "GET", "path": "books/v3/bankaccounts/{id}/statement/lastimported"},
    {"method": "GET", "path": "books/v3/bankaccounts/rules"},
    {"method": "GET", "path": "books/v3/bankaccounts/rules/{id}"},
    {"method": "GET", "path": "books/v3/banktransactions"},
    {"method": "GET", "path": "books/v3/banktransactions/uncategorized/{id}/match"},
    {"method": "GET", "path": "books/v3/banktransactions/{id}"},
    {"method": "GET", "path": "books/v3/basecurrencyadjustment"},
    {"method": "GET", "path": "books/v3/basecurrencyadjustment/accounts"},
    {"method": "GET", "path": "books/v3/basecurrencyadjustment/{id}"},
    {"method": "GET", "path": "books/v3/bills"},
    {"method": "GET", "path": "books/v3/bills/editpage/frompurchaseorders"},
    {"method": "GET", "path": "books/v3/bills/{id}"},
    {"method": "GET", "path": "books/v3/bills/{id}/attachment"},
    {"method": "GET", "path": "books/v3/bills/{id}/comments"},
    {"method": "GET", "path": "books/v3/bills/{id}/payments"},
    {"method": "GET", "path": "books/v3/chartofaccounts"},
    {"method": "GET", "path": "books/v3/chartofaccounts/transactions"},
    {"method": "GET", "path": "books/v3/chartofaccounts/{id}"},
    {"method": "GET", "path": "books/v3/contacts/{id}/contactpersons"},
    {"method": "GET", "path": "books/v3/contacts/{id}/contactpersons/{id}"},
    {"method": "GET", "path": "books/v3/contacts"},
    {"method": "GET", "path": "books/v3/contacts/{id}"},
    {"method": "GET", "path": "books/v3/contacts/{id}/address"},
    {"method": "GET", "path": "books/v3/contacts/{id}/comments"},
    {"method": "GET", "path": "books/v3/contacts/{id}/refunds"},
    {"method": "GET", "path": "books/v3/contacts/{id}/statements/email"},
    {"method": "GET", "path": "books/v3/creditnotes"},
    {"method": "GET", "path": "books/v3/creditnotes/refunds"},
    {"method": "GET", "path": "books/v3/creditnotes/templates"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/comments"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/email"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/emailhistory"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/invoices"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/refunds"},
    {"method": "GET", "path": "books/v3/creditnotes/{id}/refunds/{id}"},
    {"method": "GET", "path": "books/v3/settings/currencies"},
    {"method": "GET", "path": "books/v3/settings/currencies/{id}"},
    {"method": "GET", "path": "books/v3/settings/currencies/{id}/exchangerates"},
    {"method": "GET", "path": "books/v3/settings/currencies/{id}/exchangerates/{id}"},
    {"method": "GET", "path": "books/v3/customerpayments"},
    {"method": "GET", "path": "books/v3/customerpayments/{id}"},
    {"method": "GET", "path": "books/v3/customerpayments/{id}/refunds"},
    {"method": "GET", "path": "books/v3/customerpayments/{id}/refunds/{id}"},
    {"method": "GET", "path": "books/v3/estimates"},
    {"method": "GET", "path": "books/v3/estimates/pdf"},
    {"method": "GET", "path": "books/v3/estimates/print"},
    {"method": "GET", "path": "books/v3/estimates/templates"},
    {"method": "GET", "path": "books/v3/estimates/{id}"},
    {"method": "GET", "path": "books/v3/estimates/{id}/comments"},
    {"method": "GET", "path": "books/v3/estimates/{id}/email"},
    {"method": "GET", "path": "books/v3/employees"},
    {"method": "GET", "path": "books/v3/employees/{id}"},
    {"method": "GET", "path": "books/v3/expenses"},
    {"method": "GET", "path": "books/v3/expenses/{id}"},
    {"method": "GET", "path": "books/v3/expenses/{id}/comments"},
    {"method": "GET", "path": "books/v3/expenses/{id}/receipt"},
    {"method": "GET", "path": "books/v3/fixedassets"},
    {"method": "GET", "path": "books/v3/fixedassets/{id}"},
    {"method": "GET", "path": "books/v3/fixedassets/{id}/forecast"},
    {"method": "GET", "path": "books/v3/fixedassets/{id}/history"},
    {"method": "GET", "path": "books/v3/fixedassettypes"},
    {"method": "GET", "path": "books/v3/invoices"},
    {"method": "GET", "path": "books/v3/invoices/pdf"},
    {"method": "GET", "path": "books/v3/invoices/print"},
    {"method": "GET", "path": "books/v3/invoices/templates"},
    {"method": "GET", "path": "books/v3/invoices/{id}"},
    {"method": "GET", "path": "books/v3/invoices/{id}/attachment"},
    {"method": "GET", "path": "books/v3/invoices/{id}/comments"},
    {"method": "GET", "path": "books/v3/invoices/{id}/creditsapplied"},
    {"method": "GET", "path": "books/v3/invoices/{id}/email"},
    {"method": "GET", "path": "books/v3/invoices/{id}/paymentreminder"},
    {"method": "GET", "path": "books/v3/invoices/{id}/payments"},
    {"method": "GET", "path": "books/v3/items"},
    {"method": "GET", "path": "books/v3/items/{id}"},
    {"method": "GET", "path": "books/v3/journals"},
    {"method": "GET", "path": "books/v3/journals/{id}"},
    {"method": "GET", "path": "books/v3/locations"},
    {"method": "GET", "path": "books/v3/settings/openingbalances"},
    {"method": "GET", "path": "books/v3/organizations"},
    {"method": "GET", "path": "books/v3/organizations/{id}"},
    {"method": "GET", "path": "books/v3/projects"},
    {"method": "GET", "path": "books/v3/projects/{id}"},
    {"method": "GET", "path": "books/v3/projects/{id}/comments"},
    {"method": "GET", "path": "books/v3/projects/{id}/invoices"},
    {"method": "GET", "path": "books/v3/projects/{id}/users"},
    {"method": "GET", "path": "books/v3/projects/{id}/users/{id}"},
    {"method": "GET", "path": "books/v3/purchaseorders"},
    {"method": "GET", "path": "books/v3/purchaseorders/templates"},
    {"method": "GET", "path": "books/v3/purchaseorders/{id}"},
    {"method": "GET", "path": "books/v3/purchaseorders/{id}/attachment"},
    {"method": "GET", "path": "books/v3/purchaseorders/{id}/comments"},
    {"method": "GET", "path": "books/v3/purchaseorders/{id}/email"},
    {"method": "GET", "path": "books/v3/recurringbills"},
    {"method": "GET", "path": "books/v3/recurringbills/{id}"},
    {"method": "GET", "path": "books/v3/recurringbills/{id}/comments"},
    {"method": "GET", "path": "books/v3/recurringexpenses"},
    {"method": "GET", "path": "books/v3/recurringexpenses/{id}"},
    {"method": "GET", "path": "books/v3/recurringexpenses/{id}/comments"},
    {"method": "GET", "path": "books/v3/recurringexpenses/{id}/expenses"},
    {"method": "GET", "path": "books/v3/recurringinvoices"},
    {"method": "GET", "path": "books/v3/recurringinvoices/{id}"},
    {"method": "GET", "path": "books/v3/recurringinvoices/{id}/comments"},
    {"method": "GET", "path": "books/v3/retainerinvoices"},
    {"method": "GET", "path": "books/v3/retainerinvoices/templates"},
    {"method": "GET", "path": "books/v3/retainerinvoices/{id}"},
    {"method": "GET", "path": "books/v3/retainerinvoices/{id}/attachment"},
    {"method": "GET", "path": "books/v3/retainerinvoices/{id}/comments"},
    {"method": "GET", "path": "books/v3/retainerinvoices/{id}/email"},
    {"method": "GET", "path": "books/v3/salesorders"},
    {"method": "GET", "path": "books/v3/salesorders/pdf"},
    {"method": "GET", "path": "books/v3/salesorders/print"},
    {"method": "GET", "path": "books/v3/salesorders/templates"},
    {"method": "GET", "path": "books/v3/salesorders/{id}"},
    {"method": "GET", "path": "books/v3/salesorders/{id}/attachment"},
    {"method": "GET", "path": "books/v3/salesorders/{id}/comments"},
    {"method": "GET", "path": "books/v3/salesorders/{id}/email"},
    {"method": "GET", "path": "books/v3/salesreceipts"},
    {"method": "GET", "path": "books/v3/salesreceipts/{id}"},
    {"method": "GET", "path": "books/v3/projects/{id}/tasks"},
    {"method": "GET", "path": "books/v3/projects/{id}/tasks/{id}"},
    {"method": "GET", "path": "books/v3/settings/taxauthorities"},
    {"method": "GET", "path": "books/v3/settings/taxauthorities/{id}"},
    {"method": "GET", "path": "books/v3/settings/taxes"},
    {"method": "GET", "path": "books/v3/settings/taxes/{id}"},
    {"method": "GET", "path": "books/v3/settings/taxexemptions"},
    {"method": "GET", "path": "books/v3/settings/taxexemptions/{id}"},
    {"method": "GET", "path": "books/v3/settings/taxgroups/{id}"},
    {"method": "GET", "path": "books/v3/projects/timeentries"},
    {"method": "GET", "path": "books/v3/projects/timeentries/runningtimer/me"},
    {"method": "GET", "path": "books/v3/projects/timeentries/{id}"},
    {"method": "GET", "path": "books/v3/users"},
    {"method": "GET", "path": "books/v3/users/me"},
    {"method": "GET", "path": "books/v3/users/{id}"},
    {"method": "GET", "path": "books/v3/vendorcredits"},
    {"method": "GET", "path": "books/v3/vendorcredits/refunds"},
    {"method": "GET", "path": "books/v3/vendorcredits/{id}"},
    {"method": "GET", "path": "books/v3/vendorcredits/{id}/bills"},
    {"method": "GET", "path": "books/v3/vendorcredits/{id}/comments"},
    {"method": "GET", "path": "books/v3/vendorcredits/{id}/refunds"},
    {"method": "GET", "path": "books/v3/vendorcredits/{id}/refunds/{id}"},
    {"method": "GET", "path": "books/v3/vendorpayments"},
    {"method": "GET", "path": "books/v3/vendorpayments/{id}"},
    {"method": "GET", "path": "books/v3/vendorpayments/{id}/refunds"},
    {"method": "GET", "path": "books/v3/vendorpayments/{id}/refunds/{id}"}
  ],
  "deny": []
}
```

## Endpoints

The Zoho Books endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | books/v3/bankaccounts | read | bank-accounts | List all bank and credit card accounts for your organization. |
| POST | books/v3/bankaccounts | write | bank-accounts | Create a bank account or a credit card account for your organization. |
| GET | books/v3/bankaccounts/{id} | read | bank-accounts | Get a detailed look of the account specified. |
| PUT | books/v3/bankaccounts/{id} | write | bank-accounts | Modify the account that was created. |
| DELETE | books/v3/bankaccounts/{id} | write | bank-accounts | Delete a bank account from your organization. |
| POST | books/v3/bankaccounts/{id}/active | write | bank-accounts | Make an account active. |
| POST | books/v3/bankaccounts/{id}/inactive | write | bank-accounts | Make an account inactive. |
| GET | books/v3/bankaccounts/{id}/statement/lastimported | read | bank-accounts | Get the details of previously imported statement for the account. |
| DELETE | books/v3/bankaccounts/{id}/statement/{id} | write | bank-accounts | Delete the statement that was previously imported. |
| POST | books/v3/bankstatements | write | bank-accounts | Import your bank/credit card feeds into your account. |
| GET | books/v3/bankaccounts/rules | read | bank-rules | Fetch all the rules created for a specified bank or credit card account ID. |
| POST | books/v3/bankaccounts/rules | write | bank-rules | Create a rule and apply it on deposit/withdrawal for bank accounts and on refund/charges for credit card accounts. |
| GET | books/v3/bankaccounts/rules/{id} | read | bank-rules | Get details of a specific rule. |
| PUT | books/v3/bankaccounts/rules/{id} | write | bank-rules | Make changes to the rule, add or modify it and update. |
| DELETE | books/v3/bankaccounts/rules/{id} | write | bank-rules | Delete a rule from your account and make it no longer applicable on the transactions. |
| GET | books/v3/banktransactions | read | bank-transactions | Get all the transaction details involved in an account. |
| POST | books/v3/banktransactions | write | bank-transactions | Create a bank transaction based on the allowed transaction types. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize | write | bank-transactions | Categorize an uncategorized transaction by creating a new transaction. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/creditnoterefunds | write | bank-transactions | Categorize an Uncategorized transaction as a refund from a credit note. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/customerpayments | write | bank-transactions | Categorize an uncategorized transaction as Customer Payment. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/expenses | write | bank-transactions | Categorize an Uncategorized transaction as expense. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/paymentrefunds | write | bank-transactions | Categorizing bank transactions as Payment Refund. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/vendorcreditrefunds | write | bank-transactions | Categorize an uncategorized transaction as a refund from a vendor credit. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/vendorpaymentrefunds | write | bank-transactions | Categorizing bank transactions as Vendor Payment Refund. |
| POST | books/v3/banktransactions/uncategorized/{id}/categorize/vendorpayments | write | bank-transactions | Categorize an uncategorized transaction as Vendor Payment. |
| POST | books/v3/banktransactions/uncategorized/{id}/exclude | write | bank-transactions | Exclude a transaction from your bank or credit card account. |
| GET | books/v3/banktransactions/uncategorized/{id}/match | read | bank-transactions | Provide criteria to search for matching uncategorised transactions. |
| POST | books/v3/banktransactions/uncategorized/{id}/match | write | bank-transactions | Match an uncategorized transaction with an existing transaction in the account. |
| POST | books/v3/banktransactions/uncategorized/{id}/restore | write | bank-transactions | Restore an excluded transaction in your account. |
| GET | books/v3/banktransactions/{id} | read | bank-transactions | Fetch the details of a transaction by specifying the transaction_id. |
| PUT | books/v3/banktransactions/{id} | write | bank-transactions | Make changes in the applicable fields of a transaction and update it. |
| DELETE | books/v3/banktransactions/{id} | write | bank-transactions | Delete a transaction from an account by specifying the transaction_id. |
| POST | books/v3/banktransactions/{id}/uncategorize | write | bank-transactions | Revert a categorized transaction as uncategorized. |
| POST | books/v3/banktransactions/{id}/unmatch | write | bank-transactions | Unmatch a transaction that was previously matched and make it uncategorized. |
| GET | books/v3/basecurrencyadjustment | read | base-currency-adjustment | Lists base currency adjustment. |
| POST | books/v3/basecurrencyadjustment | write | base-currency-adjustment | Creates a base currency adjustment for the given information. |
| GET | books/v3/basecurrencyadjustment/accounts | read | base-currency-adjustment | List of accounts having transaction with effect to the given exchange rate. |
| GET | books/v3/basecurrencyadjustment/{id} | read | base-currency-adjustment | Get the base currency adjustment details. |
| DELETE | books/v3/basecurrencyadjustment/{id} | write | base-currency-adjustment | Deletes the base currency adjustment. |
| PUT | books/v3/bill/{id}/customfields | write | bills | Update the value of the custom field in existing bills. |
| GET | books/v3/bills | read | bills | List all bills with pagination. |
| POST | books/v3/bills | write | bills | Create a bill received from your vendor. |
| PUT | books/v3/bills | write | bills | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/bills/editpage/frompurchaseorders | read | bills | Create a bill for the selected purchase orders. |
| GET | books/v3/bills/{id} | read | bills | Get the details of a bill. |
| PUT | books/v3/bills/{id} | write | bills | Update a bill. |
| DELETE | books/v3/bills/{id} | write | bills | Delete an existing bill. |
| PUT | books/v3/bills/{id}/address/billing | write | bills | Updates the billing address for this bill. |
| POST | books/v3/bills/{id}/approve | write | bills | Approve a bill. |
| GET | books/v3/bills/{id}/attachment | read | bills | Returns the file attached to the bill. |
| POST | books/v3/bills/{id}/attachment | write | bills | Attach a file to a bill. |
| DELETE | books/v3/bills/{id}/attachment | write | bills | Delete the file attached to a bill. |
| GET | books/v3/bills/{id}/comments | read | bills | Get the complete history and comments of a bill. |
| POST | books/v3/bills/{id}/comments | write | bills | Add a comment for a bill. |
| DELETE | books/v3/bills/{id}/comments/{id} | write | bills | Delete a bill comment. |
| POST | books/v3/bills/{id}/credits | write | bills | Apply the vendor credits from excess vendor payments to a bill. |
| GET | books/v3/bills/{id}/payments | read | bills | Get the list of payments made for a bill. |
| DELETE | books/v3/bills/{id}/payments/{id} | write | bills | Delete a payment made to a bill. |
| POST | books/v3/bills/{id}/status/open | write | bills | Mark a void bill as open. |
| POST | books/v3/bills/{id}/status/void | write | bills | Mark a bill status as void. |
| POST | books/v3/bills/{id}/submit | write | bills | Submit a bill for approval. |
| GET | books/v3/chartofaccounts | read | chart-of-accounts | List all chart of accounts along with pagination. |
| POST | books/v3/chartofaccounts | write | chart-of-accounts | Creates an account with the given account type. |
| GET | books/v3/chartofaccounts/transactions | read | chart-of-accounts | List all involved transactions for the given account. |
| DELETE | books/v3/chartofaccounts/transactions/{id} | write | chart-of-accounts | Deletes the transaction. |
| GET | books/v3/chartofaccounts/{id} | read | chart-of-accounts | Gets the details of an account. |
| PUT | books/v3/chartofaccounts/{id} | write | chart-of-accounts | Updates the account information. |
| DELETE | books/v3/chartofaccounts/{id} | write | chart-of-accounts | Deletes the given account. |
| POST | books/v3/chartofaccounts/{id}/active | write | chart-of-accounts | Updates the account status as active. |
| POST | books/v3/chartofaccounts/{id}/inactive | write | chart-of-accounts | Updates the account status as inactive. |
| POST | books/v3/contacts/contactpersons | write | contact-persons | Create a contact person for contact. |
| PUT | books/v3/contacts/contactpersons/{id} | write | contact-persons | Update an existing contact person. |
| DELETE | books/v3/contacts/contactpersons/{id} | write | contact-persons | Delete an existing contact person. |
| POST | books/v3/contacts/contactpersons/{id}/primary | write | contact-persons | Mark a contact person as primary for the contact. |
| GET | books/v3/contacts/{id}/contactpersons | read | contact-persons | List all contacts with pagination. |
| GET | books/v3/contacts/{id}/contactpersons/{id} | read | contact-persons | Get the contact person details. |
| GET | books/v3/contacts | read | contacts | List all contacts with pagination. |
| POST | books/v3/contacts | write | contacts | Create a contact with given information. |
| PUT | books/v3/contacts | write | contacts | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/contacts/{id} | read | contacts | Get details of a contact. |
| PUT | books/v3/contacts/{id} | write | contacts | Update an existing contact. |
| DELETE | books/v3/contacts/{id} | write | contacts | Delete an existing contact. |
| POST | books/v3/contacts/{id}/active | write | contacts | Mark a contact as active. |
| GET | books/v3/contacts/{id}/address | read | contacts | Get addresses of a contact including its Shipping Address, Billing Address and other additional addresses. |
| POST | books/v3/contacts/{id}/address | write | contacts | Add an additional address for a contact using the arguments below. |
| PUT | books/v3/contacts/{id}/address/{id} | write | contacts | Edit the additional address of a contact using the arguments below. |
| DELETE | books/v3/contacts/{id}/address/{id} | write | contacts | Delete the additional address of a contact. |
| GET | books/v3/contacts/{id}/comments | read | contacts | List recent activities of a contact. |
| POST | books/v3/contacts/{id}/email | write | contacts | Send email to contact. |
| POST | books/v3/contacts/{id}/inactive | write | contacts | Mark a contact as inactive. |
| POST | books/v3/contacts/{id}/paymentreminder/disable | write | contacts | Disable automated payment reminders for a contact. |
| POST | books/v3/contacts/{id}/paymentreminder/enable | write | contacts | Enable automated payment reminders for a contact. |
| POST | books/v3/contacts/{id}/portal/enable | write | contacts | Enable portal access for a contact. |
| GET | books/v3/contacts/{id}/refunds | read | contacts | List the refund history of a contact. |
| GET | books/v3/contacts/{id}/statements/email | read | contacts | Get the statement mail content. |
| POST | books/v3/contacts/{id}/statements/email | write | contacts | Email statement to the contact. |
| POST | books/v3/contacts/{id}/track1099 | write | contacts | Track a contact for 1099 reporting: (Note: This API is only available when the organization's country is U.S.A). |
| POST | books/v3/contacts/{id}/untrack1099 | write | contacts | Use this API to stop tracking payments to a vendor for 1099 reporting. |
| GET | books/v3/creditnotes | read | credit-notes | Retrieve a paginated list of credit notes with comprehensive filtering, sorting, and search capabilities. |
| POST | books/v3/creditnotes | write | credit-notes | Create a new credit note to record credits issued to customers for returned items, overpayments, or adjustments. |
| PUT | books/v3/creditnotes | write | credit-notes | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/creditnotes/refunds | read | credit-notes | List all refunds with pagination. |
| GET | books/v3/creditnotes/templates | read | credit-notes | Get all credit note pdf templates. |
| GET | books/v3/creditnotes/{id} | read | credit-notes | Details of an existing creditnote. |
| PUT | books/v3/creditnotes/{id} | write | credit-notes | Details of an existing creditnote. |
| DELETE | books/v3/creditnotes/{id} | write | credit-notes | Delete an existing credit note. |
| PUT | books/v3/creditnotes/{id}/address/billing | write | credit-notes | Updates the billing address for an existing credit note alone. |
| PUT | books/v3/creditnotes/{id}/address/shipping | write | credit-notes | Updates the shipping address for an existing credit note alone. |
| POST | books/v3/creditnotes/{id}/approve | write | credit-notes | Approve a credit note. |
| GET | books/v3/creditnotes/{id}/comments | read | credit-notes | Get history and comments of a credit note. |
| POST | books/v3/creditnotes/{id}/comments | write | credit-notes | Add a comment to an existing credit note. |
| DELETE | books/v3/creditnotes/{id}/comments/{id} | write | credit-notes | Delete a credit note comment. |
| GET | books/v3/creditnotes/{id}/email | read | credit-notes | Get email content of a credit note. |
| POST | books/v3/creditnotes/{id}/email | write | credit-notes | Email a credit note. |
| GET | books/v3/creditnotes/{id}/emailhistory | read | credit-notes | Get email history of a credit code. |
| GET | books/v3/creditnotes/{id}/invoices | read | credit-notes | List invoices to which the credit note is applied. |
| POST | books/v3/creditnotes/{id}/invoices | write | credit-notes | Apply credit note to existing invoices. |
| DELETE | books/v3/creditnotes/{id}/invoices/{id} | write | credit-notes | Delete the credits applied to an invoice. |
| GET | books/v3/creditnotes/{id}/refunds | read | credit-notes | List all refunds of an existing credit note. |
| POST | books/v3/creditnotes/{id}/refunds | write | credit-notes | Refund credit note amount. |
| GET | books/v3/creditnotes/{id}/refunds/{id} | read | credit-notes | Get refund of a particular credit note. |
| PUT | books/v3/creditnotes/{id}/refunds/{id} | write | credit-notes | Update the refunded transaction. |
| DELETE | books/v3/creditnotes/{id}/refunds/{id} | write | credit-notes | Delete a credit note refund. |
| POST | books/v3/creditnotes/{id}/status/draft | write | credit-notes | Convert a voided credit note to Draft. |
| POST | books/v3/creditnotes/{id}/status/open | write | credit-notes | Convert a credit note in Draft status to Open. |
| POST | books/v3/creditnotes/{id}/status/void | write | credit-notes | Mark the credit note as Void. |
| POST | books/v3/creditnotes/{id}/submit | write | credit-notes | Submit an estimate for approval. |
| PUT | books/v3/creditnotes/{id}/templates/{id} | write | credit-notes | Update the pdf template associated with the credit note. |
| GET | books/v3/settings/currencies | read | currencies | Get list of currencies configured. |
| POST | books/v3/settings/currencies | write | currencies | Create a currency for transaction. |
| GET | books/v3/settings/currencies/{id} | read | currencies | Get the details of a currency. |
| PUT | books/v3/settings/currencies/{id} | write | currencies | Update the details of a currency. |
| DELETE | books/v3/settings/currencies/{id} | write | currencies | Delete a currency. |
| GET | books/v3/settings/currencies/{id}/exchangerates | read | currencies | List of exchange rates configured for the currency. |
| POST | books/v3/settings/currencies/{id}/exchangerates | write | currencies | Create an exchange rate for the specified currency. |
| GET | books/v3/settings/currencies/{id}/exchangerates/{id} | read | currencies | Get the details of an exchange rate that has been asscoiated to the currency. |
| PUT | books/v3/settings/currencies/{id}/exchangerates/{id} | write | currencies | Update the details of exchange rate for a currency. |
| DELETE | books/v3/settings/currencies/{id}/exchangerates/{id} | write | currencies | Delete an exchange rate for the specified currency. |
| PUT | books/v3/customerpayment/{id}/customfields | write | customer-payments | Update the value of the custom field in existing customerpayments. |
| GET | books/v3/customerpayments | read | customer-payments | List all the payments made by your customer. |
| POST | books/v3/customerpayments | write | customer-payments | Create a new payment. |
| PUT | books/v3/customerpayments | write | customer-payments | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/customerpayments/{id} | read | customer-payments | Details of an existing payment. |
| PUT | books/v3/customerpayments/{id} | write | customer-payments | Update an existing payment information. |
| DELETE | books/v3/customerpayments/{id} | write | customer-payments | Delete an existing payment. |
| GET | books/v3/customerpayments/{id}/refunds | read | customer-payments | List all the refunds pertaining to an existing customer payment. |
| POST | books/v3/customerpayments/{id}/refunds | write | customer-payments | Refund the excess amount paid by the customer. |
| GET | books/v3/customerpayments/{id}/refunds/{id} | read | customer-payments | Obtain details of a particular refund of a customer payment. |
| PUT | books/v3/customerpayments/{id}/refunds/{id} | write | customer-payments | Update the refunded transaction. |
| DELETE | books/v3/customerpayments/{id}/refunds/{id} | write | customer-payments | Delete refund pertaining to an existing customer payment. |
| PUT | books/v3/estimate/{id}/customfields | write | estimates | Update the value of the custom field in existing estimates. |
| GET | books/v3/estimates | read | estimates | List all estimates with pagination. |
| POST | books/v3/estimates | write | estimates | Create an estimate for your customer. |
| PUT | books/v3/estimates | write | estimates | A custom field will have unique values if it's configured to not accept duplicate values. |
| POST | books/v3/estimates/email | write | estimates | Send estimates to your customers by email. |
| GET | books/v3/estimates/pdf | read | estimates | Maximum of 25 estimates can be exported in a single pdf. |
| GET | books/v3/estimates/print | read | estimates | Export estimates as pdf and print them. |
| GET | books/v3/estimates/templates | read | estimates | Get all estimate pdf templates. |
| GET | books/v3/estimates/{id} | read | estimates | Get the details of an estimate. |
| PUT | books/v3/estimates/{id} | write | estimates | Update an existing estimate. |
| DELETE | books/v3/estimates/{id} | write | estimates | Delete an existing estimate. |
| PUT | books/v3/estimates/{id}/address/billing | write | estimates | Updates the billing address for this estimate alone. |
| PUT | books/v3/estimates/{id}/address/shipping | write | estimates | Updates the shipping address for an existing estimate alone. |
| POST | books/v3/estimates/{id}/approve | write | estimates | Approve an estimate. |
| GET | books/v3/estimates/{id}/comments | read | estimates | Get the complete history and comments of an estimate. |
| POST | books/v3/estimates/{id}/comments | write | estimates | Add a comment for an estimate. |
| PUT | books/v3/estimates/{id}/comments/{id} | write | estimates | Update an existing comment of an estimate. |
| DELETE | books/v3/estimates/{id}/comments/{id} | write | estimates | Delete an estimate comment. |
| GET | books/v3/estimates/{id}/email | read | estimates | Get the email content of an estimate. |
| POST | books/v3/estimates/{id}/email | write | estimates | Email an estimate to the customer. |
| POST | books/v3/estimates/{id}/status/accepted | write | estimates | Mark a sent estimate as accepted if the customer has accepted it. |
| POST | books/v3/estimates/{id}/status/declined | write | estimates | Mark a sent estimate as declined if the customer has rejected it. |
| POST | books/v3/estimates/{id}/status/sent | write | estimates | Mark a draft estimate as sent. |
| POST | books/v3/estimates/{id}/submit | write | estimates | Submit an estimate for approval. |
| PUT | books/v3/estimates/{id}/templates/{id} | write | estimates | Update the pdf template associated with the estimate. |
| DELETE | books/v3/employee/{id} | write | expenses | Delete an existing employee. |
| GET | books/v3/employees | read | expenses | List employees with pagination. |
| POST | books/v3/employees | write | expenses | Create an employee for an expense. |
| GET | books/v3/employees/{id} | read | expenses | Get the details of the employee. |
| GET | books/v3/expenses | read | expenses | List all the Expenses with pagination. |
| POST | books/v3/expenses | write | expenses | Create billable or non-billable expense. |
| PUT | books/v3/expenses | write | expenses | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/expenses/{id} | read | expenses | Get the details of the Expense. |
| PUT | books/v3/expenses/{id} | write | expenses | Update an existing Expense. |
| DELETE | books/v3/expenses/{id} | write | expenses | Delete an existing expense. |
| GET | books/v3/expenses/{id}/comments | read | expenses | Get history and comments of expense. |
| GET | books/v3/expenses/{id}/receipt | read | expenses | Returns the receipt attached to the expense. |
| POST | books/v3/expenses/{id}/receipt | write | expenses | Attach a receipt to an expense. |
| DELETE | books/v3/expenses/{id}/receipt | write | expenses | Delete the receipt attached to the expense. |
| GET | books/v3/fixedassets | read | fixed-assets | fixed asset list. |
| POST | books/v3/fixedassets | write | fixed-assets | Create a fixed asset. |
| GET | books/v3/fixedassets/{id} | read | fixed-assets | Get the details of the fixed asset. |
| PUT | books/v3/fixedassets/{id} | write | fixed-assets | Updates the fixed asset with given information. |
| DELETE | books/v3/fixedassets/{id} | write | fixed-assets | Deletes the given fixed asset. |
| POST | books/v3/fixedassets/{id}/comments | write | fixed-assets | Add a comment to the fixed asset. |
| DELETE | books/v3/fixedassets/{id}/comments/{id} | write | fixed-assets | Delete the comment of the fixed asset. |
| GET | books/v3/fixedassets/{id}/forecast | read | fixed-assets | It displays a detailed summary of the asset's future depreciation rates. |
| GET | books/v3/fixedassets/{id}/history | read | fixed-assets | It displays a detailed summary of the asset from acquisition till write off. |
| POST | books/v3/fixedassets/{id}/sell | write | fixed-assets | Sell the fixed asset. |
| POST | books/v3/fixedassets/{id}/status/active | write | fixed-assets | Mark the fixed asset as active to start calculating depreciation for the asset. |
| POST | books/v3/fixedassets/{id}/status/cancel | write | fixed-assets | Cancel the fixed asset. |
| POST | books/v3/fixedassets/{id}/status/draft | write | fixed-assets | Mark the fixed asset as draft. |
| POST | books/v3/fixedassets/{id}/writeoff | write | fixed-assets | Write off the fixed asset. |
| GET | books/v3/fixedassettypes | read | fixed-assets | fixed asset type list. |
| POST | books/v3/fixedassettypes | write | fixed-assets | Create a fixed asset type. |
| PUT | books/v3/fixedassettypes/{id} | write | fixed-assets | Updates the fixed asset type with given information. |
| DELETE | books/v3/fixedassettypes/{id} | write | fixed-assets | Deletes the given fixed asset type. |
| PUT | books/v3/invoice/{id}/customfields | write | invoices | Update the value of the custom field in existing invoices. |
| GET | books/v3/invoices | read | invoices | List all invoices with pagination. |
| POST | books/v3/invoices | write | invoices | Create an invoice for your customer. |
| PUT | books/v3/invoices | write | invoices | A custom field will have unique values if it's configured to not accept duplicate values. |
| POST | books/v3/invoices/email | write | invoices | Send invoices to your customers by email. |
| DELETE | books/v3/invoices/expenses/{id}/receipt | write | invoices | Delete the expense receipts attached to an invoice which is raised from an expense. |
| POST | books/v3/invoices/fromsalesorder | write | invoices | Create an instant invoice for all the confirmed sales orders you have selected. |
| POST | books/v3/invoices/paymentreminder | write | invoices | Remind your customer about an unpaid invoices by email. |
| GET | books/v3/invoices/pdf | read | invoices | Maximum of 25 invoices can be exported in a single pdf. |
| GET | books/v3/invoices/print | read | invoices | Export invoices as pdf and print them. |
| GET | books/v3/invoices/templates | read | invoices | Get all invoice pdf templates. |
| GET | books/v3/invoices/{id} | read | invoices | Get the details of an invoice. |
| PUT | books/v3/invoices/{id} | write | invoices | Update an existing invoice. |
| DELETE | books/v3/invoices/{id} | write | invoices | Delete an existing invoice. |
| PUT | books/v3/invoices/{id}/address/billing | write | invoices | Updates the billing address for this invoice alone. |
| PUT | books/v3/invoices/{id}/address/shipping | write | invoices | Updates the shipping address for this invoice alone. |
| POST | books/v3/invoices/{id}/approve | write | invoices | Approve an invoice. |
| GET | books/v3/invoices/{id}/attachment | read | invoices | Returns the file attached to the invoice. |
| POST | books/v3/invoices/{id}/attachment | write | invoices | Attach a file to an invoice. |
| PUT | books/v3/invoices/{id}/attachment | write | invoices | Set whether you want to send the attached file while emailing the invoice. |
| DELETE | books/v3/invoices/{id}/attachment | write | invoices | Delete the file attached to the invoice. |
| GET | books/v3/invoices/{id}/comments | read | invoices | Get the complete history and comments of an invoice. |
| POST | books/v3/invoices/{id}/comments | write | invoices | Add a comment for an invoice. |
| PUT | books/v3/invoices/{id}/comments/{id} | write | invoices | Update an existing comment of an invoice. |
| DELETE | books/v3/invoices/{id}/comments/{id} | write | invoices | Delete an invoice comment. |
| POST | books/v3/invoices/{id}/credits | write | invoices | Apply the customer credits either from credit notes or excess customer payments to an invoice. |
| GET | books/v3/invoices/{id}/creditsapplied | read | invoices | Get the list of credits applied for an invoice. |
| DELETE | books/v3/invoices/{id}/creditsapplied/{id} | write | invoices | Delete a particular credit applied to an invoice. |
| GET | books/v3/invoices/{id}/email | read | invoices | Get the email content of an invoice. |
| POST | books/v3/invoices/{id}/email | write | invoices | Email an invoice to the customer. |
| GET | books/v3/invoices/{id}/paymentreminder | read | invoices | Get the mail content of the payment reminder. |
| POST | books/v3/invoices/{id}/paymentreminder | write | invoices | Remind your customer about an unpaid invoice by email. |
| POST | books/v3/invoices/{id}/paymentreminder/disable | write | invoices | Disable automated payment reminders for an invoice. |
| POST | books/v3/invoices/{id}/paymentreminder/enable | write | invoices | Enable automated payment reminders for an invoice. |
| GET | books/v3/invoices/{id}/payments | read | invoices | Get the list of payments made for an invoice. |
| DELETE | books/v3/invoices/{id}/payments/{id} | write | invoices | Delete a payment made to an invoice. |
| POST | books/v3/invoices/{id}/status/draft | write | invoices | Mark a voided invoice as draft. |
| POST | books/v3/invoices/{id}/status/sent | write | invoices | Mark a draft invoice as sent. |
| POST | books/v3/invoices/{id}/status/void | write | invoices | Mark an invoice status as void. |
| POST | books/v3/invoices/{id}/submit | write | invoices | Submit an invoice for approval. |
| PUT | books/v3/invoices/{id}/templates/{id} | write | invoices | Update the pdf template associated with the invoice. |
| POST | books/v3/invoices/{id}/writeoff | write | invoices | Write off the invoice balance amount of an invoice. |
| POST | books/v3/invoices/{id}/writeoff/cancel | write | invoices | Cancel the write off amount of an invoice. |
| GET | books/v3/share/paymentlink | write | invoices | This API generates a payment link for the invoice with an expiry date. Kept out of read: generates a shareable payment link. |
| PUT | books/v3/item/{id}/customfields | write | items | Update the value of the custom field in existing items. |
| GET | books/v3/items | read | items | Get the list of all active items with pagination. |
| POST | books/v3/items | write | items | Create a new item. |
| PUT | books/v3/items | write | items | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/items/{id} | read | items | Details of an existing item. |
| PUT | books/v3/items/{id} | write | items | Update the details of an item. |
| DELETE | books/v3/items/{id} | write | items | Delete the item created.items that are part of transaction cannot be deleted. |
| POST | books/v3/items/{id}/active | write | items | Mark an inactive item as active. |
| POST | books/v3/items/{id}/inactive | write | items | Mark an active item as inactive. |
| GET | books/v3/journals | read | journals | Get journal list. |
| POST | books/v3/journals | write | journals | Create a journal. |
| GET | books/v3/journals/{id} | read | journals | Get the details of the journal. |
| PUT | books/v3/journals/{id} | write | journals | Updates the journal with given information. |
| DELETE | books/v3/journals/{id} | write | journals | Deletes the given journal. |
| POST | books/v3/journals/{id}/attachment | write | journals | Attach a file to a journal. |
| POST | books/v3/journals/{id}/comments | write | journals | Add a comment for a journal. |
| DELETE | books/v3/journals/{id}/comments/{id} | write | journals | Delete a jounral comment. |
| POST | books/v3/journals/{id}/status/publish | write | journals | Mark a draft journal as published. |
| GET | books/v3/locations | read | locations | List all the available locations in your zoho inventory. |
| POST | books/v3/locations | write | locations | Create a location. |
| PUT | books/v3/locations/{id} | write | locations | Update location. |
| DELETE | books/v3/locations/{id} | write | locations | Delete a location. |
| POST | books/v3/locations/{id}/active | write | locations | Mark location as Active. |
| POST | books/v3/locations/{id}/inactive | write | locations | Mark location as Inactive. |
| POST | books/v3/locations/{id}/markasprimary | write | locations | Mark location as primary. |
| POST | books/v3/settings/locations/enable | write | locations | Enable Locations for an organisation. |
| GET | books/v3/settings/openingbalances | read | opening-balance | Get opening balance. |
| POST | books/v3/settings/openingbalances | write | opening-balance | Creates opening balance with the given information. |
| PUT | books/v3/settings/openingbalances | write | opening-balance | Updates the existing opening balance information. |
| DELETE | books/v3/settings/openingbalances | write | opening-balance | Delete the entered opening balance. |
| GET | books/v3/organizations | read | organizations | Get the list of organizations. |
| POST | books/v3/organizations | write | organizations | Create an organization. |
| GET | books/v3/organizations/{id} | read | organizations | Get the details of an organization. |
| PUT | books/v3/organizations/{id} | write | organizations | Update the details of an organization. |
| GET | books/v3/projects | read | projects | List all projects with pagination. |
| POST | books/v3/projects | write | projects | Create a project. |
| PUT | books/v3/projects | write | projects | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/projects/{id} | read | projects | Get the details of a project. |
| PUT | books/v3/projects/{id} | write | projects | Update details of a project. |
| DELETE | books/v3/projects/{id} | write | projects | Deleting a existing project. |
| POST | books/v3/projects/{id}/active | write | projects | Mark project as active. |
| POST | books/v3/projects/{id}/clone | write | projects | Cloning a project. |
| GET | books/v3/projects/{id}/comments | read | projects | Get comments for a project. |
| POST | books/v3/projects/{id}/comments | write | projects | Post comment to a project. |
| DELETE | books/v3/projects/{id}/comments/{id} | write | projects | Deleting a comment. |
| POST | books/v3/projects/{id}/inactive | write | projects | Marking a project as inactive. |
| GET | books/v3/projects/{id}/invoices | read | projects | Lists invoices created for this project. |
| GET | books/v3/projects/{id}/users | read | projects | Get list of users associated with a project. |
| POST | books/v3/projects/{id}/users | write | projects | Assign a users to a project. |
| POST | books/v3/projects/{id}/users/invite | write | projects | Invite and user to the project. |
| GET | books/v3/projects/{id}/users/{id} | read | projects | Get details of a user in project. |
| PUT | books/v3/projects/{id}/users/{id} | write | projects | Update details of a user. |
| DELETE | books/v3/projects/{id}/users/{id} | write | projects | Remove user from a project. |
| PUT | books/v3/purchaseorder/{id}/customfields | write | purchase-orders | Update the value of the custom field in existing purchaseorders. |
| GET | books/v3/purchaseorders | read | purchase-orders | List all purchase orders. |
| POST | books/v3/purchaseorders | write | purchase-orders | Create a purchase order for your vendor. |
| PUT | books/v3/purchaseorders | write | purchase-orders | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/purchaseorders/templates | read | purchase-orders | Get all purchase order pdf templates. |
| GET | books/v3/purchaseorders/{id} | read | purchase-orders | Get the details of a purchase order. |
| PUT | books/v3/purchaseorders/{id} | write | purchase-orders | Update an existing purchase order. |
| DELETE | books/v3/purchaseorders/{id} | write | purchase-orders | Delete an existing purchase order. |
| PUT | books/v3/purchaseorders/{id}/address/billing | write | purchase-orders | Updates the billing address for this purchase order alone. |
| POST | books/v3/purchaseorders/{id}/approve | write | purchase-orders | Approve a purchase order. |
| GET | books/v3/purchaseorders/{id}/attachment | read | purchase-orders | Returns the file attached to the purchase order. |
| POST | books/v3/purchaseorders/{id}/attachment | write | purchase-orders | Attach a file to a purchase order. |
| PUT | books/v3/purchaseorders/{id}/attachment | write | purchase-orders | Set whether you want to send the attached file while emailing the purchase order. |
| DELETE | books/v3/purchaseorders/{id}/attachment | write | purchase-orders | Delete the file attached to the purchase order. |
| GET | books/v3/purchaseorders/{id}/comments | read | purchase-orders | Get the complete history and comments of purchase order. |
| POST | books/v3/purchaseorders/{id}/comments | write | purchase-orders | Add a comment for a purchase order. |
| PUT | books/v3/purchaseorders/{id}/comments/{id} | write | purchase-orders | Update an existing comment of a purchase order. |
| DELETE | books/v3/purchaseorders/{id}/comments/{id} | write | purchase-orders | Delete a purchase order comment. |
| GET | books/v3/purchaseorders/{id}/email | read | purchase-orders | Get the email content of a purchase order. |
| POST | books/v3/purchaseorders/{id}/email | write | purchase-orders | Email a purchase order to the vendor. |
| POST | books/v3/purchaseorders/{id}/reject | write | purchase-orders | Reject a purchase order. |
| POST | books/v3/purchaseorders/{id}/status/billed | write | purchase-orders | Mark a purchase order as billed. |
| POST | books/v3/purchaseorders/{id}/status/cancelled | write | purchase-orders | Mark a purchase order as cancelled. |
| POST | books/v3/purchaseorders/{id}/status/open | write | purchase-orders | Mark a draft purchase order as open. |
| POST | books/v3/purchaseorders/{id}/submit | write | purchase-orders | Submit a purchase order for approval. |
| PUT | books/v3/purchaseorders/{id}/templates/{id} | write | purchase-orders | Update the pdf template associated with the purchase order. |
| GET | books/v3/recurringbills | read | recurring-bills | List all recurring bills with pagination. |
| POST | books/v3/recurringbills | write | recurring-bills | Create a recurring bill. |
| PUT | books/v3/recurringbills | write | recurring-bills | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/recurringbills/{id} | read | recurring-bills | Get the details of a recurring bill. |
| PUT | books/v3/recurringbills/{id} | write | recurring-bills | Update a recurring bill. |
| DELETE | books/v3/recurringbills/{id} | write | recurring-bills | Delete an existing recurring bill. |
| GET | books/v3/recurringbills/{id}/comments | read | recurring-bills | Get history and comments of a recurring bill. |
| POST | books/v3/recurringbills/{id}/status/resume | write | recurring-bills | Resume a stopped recurring bill. |
| POST | books/v3/recurringbills/{id}/status/stop | write | recurring-bills | Stop an active recurring bill. |
| GET | books/v3/recurringexpenses | read | recurring-expenses | List all the Expenses with pagination. |
| POST | books/v3/recurringexpenses | write | recurring-expenses | Create a recurring expense. |
| PUT | books/v3/recurringexpenses | write | recurring-expenses | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/recurringexpenses/{id} | read | recurring-expenses | Get the details of the recurring expense. |
| PUT | books/v3/recurringexpenses/{id} | write | recurring-expenses | Update a recurring expense. |
| DELETE | books/v3/recurringexpenses/{id} | write | recurring-expenses | Deleting an existing recurring expense. |
| GET | books/v3/recurringexpenses/{id}/comments | read | recurring-expenses | Get history and comments of a recurring expense. |
| GET | books/v3/recurringexpenses/{id}/expenses | read | recurring-expenses | List child expenses created from recurring expense. |
| POST | books/v3/recurringexpenses/{id}/status/resume | write | recurring-expenses | Resume a stopped recurring expense. |
| POST | books/v3/recurringexpenses/{id}/status/stop | write | recurring-expenses | Stop an active recurring expense. |
| GET | books/v3/recurringinvoices | read | recurring-invoices | List the details of all recurring invoice. |
| POST | books/v3/recurringinvoices | write | recurring-invoices | Creating a new recurring invoice. |
| PUT | books/v3/recurringinvoices | write | recurring-invoices | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/recurringinvoices/{id} | read | recurring-invoices | Get the details of a recurring invoice. |
| PUT | books/v3/recurringinvoices/{id} | write | recurring-invoices | Update the recurring invoice. |
| DELETE | books/v3/recurringinvoices/{id} | write | recurring-invoices | Delete an existing recurring invoice. |
| GET | books/v3/recurringinvoices/{id}/comments | read | recurring-invoices | Get the complete history and comments of a recurring invoice. |
| POST | books/v3/recurringinvoices/{id}/status/resume | write | recurring-invoices | Resume a stopped recurring invoice. |
| POST | books/v3/recurringinvoices/{id}/status/stop | write | recurring-invoices | Stop an active recurring invoice. |
| PUT | books/v3/recurringinvoices/{id}/templates/{id} | write | recurring-invoices | Update the pdf template associated with the recurring invoice. |
| GET | books/v3/retainerinvoices | read | retainer-invoices | List all retainer invoices with pagination. |
| POST | books/v3/retainerinvoices | write | retainer-invoices | Create a retainer invoice for your customer. |
| GET | books/v3/retainerinvoices/templates | read | retainer-invoices | Get all retainer invoice pdf templates. |
| GET | books/v3/retainerinvoices/{id} | read | retainer-invoices | Get the details of a retainer invoice. |
| PUT | books/v3/retainerinvoices/{id} | write | retainer-invoices | Update an existing invoice. |
| DELETE | books/v3/retainerinvoices/{id} | write | retainer-invoices | Delete an existing retainer invoice. |
| PUT | books/v3/retainerinvoices/{id}/address/billing | write | retainer-invoices | Updates the billing address for this retainer invoice alone. |
| POST | books/v3/retainerinvoices/{id}/approve | write | retainer-invoices | Approve a retainer invoice. |
| GET | books/v3/retainerinvoices/{id}/attachment | read | retainer-invoices | Returns the file attached to the retainer invoice. |
| POST | books/v3/retainerinvoices/{id}/attachment | write | retainer-invoices | Attach a file to an invoice. |
| GET | books/v3/retainerinvoices/{id}/comments | read | retainer-invoices | Get the complete history and comments of a retainer invoice. |
| POST | books/v3/retainerinvoices/{id}/comments | write | retainer-invoices | Add a comment for a retainer invoice. |
| PUT | books/v3/retainerinvoices/{id}/comments/{id} | write | retainer-invoices | Update an existing comment of a retainer invoice. |
| DELETE | books/v3/retainerinvoices/{id}/comments/{id} | write | retainer-invoices | Delete a retainer invoice comment. |
| DELETE | books/v3/retainerinvoices/{id}/documents/{id} | write | retainer-invoices | Delete the file attached to the retainer invoice. |
| GET | books/v3/retainerinvoices/{id}/email | read | retainer-invoices | Get the email content of a retainer invoice. |
| POST | books/v3/retainerinvoices/{id}/email | write | retainer-invoices | Email a retainer invoice to the customer. |
| POST | books/v3/retainerinvoices/{id}/status/draft | write | retainer-invoices | Mark a voided retainer invoice as draft. |
| POST | books/v3/retainerinvoices/{id}/status/sent | write | retainer-invoices | Mark a draft retainer invoice as sent. |
| POST | books/v3/retainerinvoices/{id}/status/void | write | retainer-invoices | Mark an invoice status as void. |
| POST | books/v3/retainerinvoices/{id}/submit | write | retainer-invoices | Submit a retainer invoice for approval. |
| PUT | books/v3/retainerinvoices/{id}/templates/{id} | write | retainer-invoices | Update the pdf template associated with the retainer invoice. |
| PUT | books/v3/salesorder/{id}/customfields | write | sales-orders | Update the value of the custom field in existing salesorders. |
| GET | books/v3/salesorders | read | sales-orders | List all sales orders. |
| POST | books/v3/salesorders | write | sales-orders | Create a sales order for your customer. |
| PUT | books/v3/salesorders | write | sales-orders | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/salesorders/pdf | read | sales-orders | Maximum of 25 sales orders can be exported in a single pdf. |
| GET | books/v3/salesorders/print | read | sales-orders | Export sales orders as pdf and print them. |
| GET | books/v3/salesorders/templates | read | sales-orders | Get all sales order pdf templates. |
| GET | books/v3/salesorders/{id} | read | sales-orders | Get the details of a sales order. |
| PUT | books/v3/salesorders/{id} | write | sales-orders | Update an existing sales order. |
| DELETE | books/v3/salesorders/{id} | write | sales-orders | Delete an existing sales order. |
| PUT | books/v3/salesorders/{id}/address/billing | write | sales-orders | Updates the billing address for this sales order alone. |
| PUT | books/v3/salesorders/{id}/address/shipping | write | sales-orders | Updates the shipping address for this sales order alone. |
| POST | books/v3/salesorders/{id}/approve | write | sales-orders | Approve a sales order. |
| GET | books/v3/salesorders/{id}/attachment | read | sales-orders | Returns the file attached to the sales order. |
| POST | books/v3/salesorders/{id}/attachment | write | sales-orders | Attach a file to a sales order. |
| PUT | books/v3/salesorders/{id}/attachment | write | sales-orders | Set whether you want to send the attached file while emailing the sales order. |
| DELETE | books/v3/salesorders/{id}/attachment | write | sales-orders | Delete the file attached to the sales order. |
| GET | books/v3/salesorders/{id}/comments | read | sales-orders | Get the complete history and comments of sales order. |
| POST | books/v3/salesorders/{id}/comments | write | sales-orders | Add a comment for a sales order. |
| PUT | books/v3/salesorders/{id}/comments/{id} | write | sales-orders | Update existing comment of a sales order. |
| DELETE | books/v3/salesorders/{id}/comments/{id} | write | sales-orders | Delete a sales order comment. |
| GET | books/v3/salesorders/{id}/email | read | sales-orders | Get the email content of a sales order. |
| POST | books/v3/salesorders/{id}/email | write | sales-orders | Email a sales order to the customer. |
| POST | books/v3/salesorders/{id}/status/open | write | sales-orders | Mark a draft sales order as open. |
| POST | books/v3/salesorders/{id}/status/void | write | sales-orders | Mark a sales order as void. |
| POST | books/v3/salesorders/{id}/submit | write | sales-orders | Submit a sales order for approval. |
| POST | books/v3/salesorders/{id}/substatus/cs_openshi | write | sales-orders | Update a sales order sub status. |
| PUT | books/v3/salesorders/{id}/templates/{id} | write | sales-orders | Update the pdf template associated with the sales order. |
| GET | books/v3/salesreceipts | read | sales-receipt | List all sales receipts. |
| POST | books/v3/salesreceipts | write | sales-receipt | Create a sales receipt for immediate payment transactions. |
| GET | books/v3/salesreceipts/{id} | read | sales-receipt | Get the details of a sales receipt. |
| PUT | books/v3/salesreceipts/{id} | write | sales-receipt | Update an existing sales receipt. |
| DELETE | books/v3/salesreceipts/{id} | write | sales-receipt | Delete an existing sales receipt. |
| POST | books/v3/salesreceipts/{id}/email | write | sales-receipt | Email a sales receipt to the customer. |
| GET | books/v3/projects/{id}/tasks | read | tasks | Get list of tasks added to a project. |
| POST | books/v3/projects/{id}/tasks | write | tasks | The task has been added. |
| GET | books/v3/projects/{id}/tasks/{id} | read | tasks | Get the details of a task. |
| PUT | books/v3/projects/{id}/tasks/{id} | write | tasks | Update the details of a task. |
| DELETE | books/v3/projects/{id}/tasks/{id} | write | tasks | Delete a task added to a project. |
| GET | books/v3/settings/taxauthorities | read | taxes | List of tax authorities. |
| POST | books/v3/settings/taxauthorities | write | taxes | Create a tax authority. |
| GET | books/v3/settings/taxauthorities/{id} | read | taxes | Get the details of a tax authority. |
| PUT | books/v3/settings/taxauthorities/{id} | write | taxes | Update the details of a tax authority. |
| DELETE | books/v3/settings/taxauthorities/{id} | write | taxes | Delete a tax authority. |
| GET | books/v3/settings/taxes | read | taxes | List of simple and compound taxes with pagination. |
| POST | books/v3/settings/taxes | write | taxes | Create a tax which can be associated with an item. |
| GET | books/v3/settings/taxes/{id} | read | taxes | Get the details of a simple or compound tax. |
| PUT | books/v3/settings/taxes/{id} | write | taxes | Update the details of a simple or compound tax. |
| DELETE | books/v3/settings/taxes/{id} | write | taxes | Delete a simple or compound tax. |
| GET | books/v3/settings/taxexemptions | read | taxes | List of tax exemptions. |
| POST | books/v3/settings/taxexemptions | write | taxes | Create a tax exemption. |
| GET | books/v3/settings/taxexemptions/{id} | read | taxes | Get the details of a tax exemption. |
| PUT | books/v3/settings/taxexemptions/{id} | write | taxes | Update the details of a tax exemption. |
| DELETE | books/v3/settings/taxexemptions/{id} | write | taxes | Delete a tax exemption. |
| POST | books/v3/settings/taxgroups | write | taxes | Create a tax group associating multiple taxes. |
| GET | books/v3/settings/taxgroups/{id} | read | taxes | Get the details of a tax group. |
| PUT | books/v3/settings/taxgroups/{id} | write | taxes | Update the details of the tax group. |
| DELETE | books/v3/settings/taxgroups/{id} | write | taxes | Delete a tax group. |
| GET | books/v3/projects/timeentries | read | time-entries | List all time entries with pagination. |
| POST | books/v3/projects/timeentries | write | time-entries | Logging time entries. |
| DELETE | books/v3/projects/timeentries | write | time-entries | Deleting time entries. |
| GET | books/v3/projects/timeentries/runningtimer/me | read | time-entries | Get current running timer. |
| POST | books/v3/projects/timeentries/timer/stop | write | time-entries | Stop tracking time, say taking a break or leaving. |
| GET | books/v3/projects/timeentries/{id} | read | time-entries | Get details of a time entry. |
| PUT | books/v3/projects/timeentries/{id} | write | time-entries | Update logged time entry. |
| DELETE | books/v3/projects/timeentries/{id} | write | time-entries | Deleting a logged time entry. |
| POST | books/v3/projects/timeentries/{id}/timer/start | write | time-entries | Start tracking time spent. |
| GET | books/v3/users | read | users | Get the list of all users in the organization. |
| POST | books/v3/users | write | users | Create a user for your organization. |
| GET | books/v3/users/me | read | users | Get the details of the current user. |
| GET | books/v3/users/{id} | read | users | Get the details of a user. |
| PUT | books/v3/users/{id} | write | users | Update the details of a user. |
| DELETE | books/v3/users/{id} | write | users | Delete a user associated to the organization. |
| POST | books/v3/users/{id}/active | write | users | Mark an inactive user as active. |
| POST | books/v3/users/{id}/inactive | write | users | Mark an active user as inactive. |
| POST | books/v3/users/{id}/invite | write | users | Send invitation email to a user. |
| GET | books/v3/vendorcredits | read | vendor-credits | List vendor credits with pagination. |
| POST | books/v3/vendorcredits | write | vendor-credits | Create a vendor credit for a vendor. |
| GET | books/v3/vendorcredits/refunds | read | vendor-credits | List all refunds with pagination. |
| GET | books/v3/vendorcredits/{id} | read | vendor-credits | Get details of a vendor credit. |
| PUT | books/v3/vendorcredits/{id} | write | vendor-credits | Update an existing vendor credit. |
| DELETE | books/v3/vendorcredits/{id} | write | vendor-credits | Delete a vendor credit. |
| POST | books/v3/vendorcredits/{id}/approve | write | vendor-credits | Approve a Vendor credit. |
| GET | books/v3/vendorcredits/{id}/bills | read | vendor-credits | List bills to which the vendor credit is applied. |
| POST | books/v3/vendorcredits/{id}/bills | write | vendor-credits | Apply vendor credit to existing bills. |
| DELETE | books/v3/vendorcredits/{id}/bills/{id} | write | vendor-credits | Delete the credits applied to a bill. |
| GET | books/v3/vendorcredits/{id}/comments | read | vendor-credits | Get history and comments of a vendor credit. |
| POST | books/v3/vendorcredits/{id}/comments | write | vendor-credits | Add a comment to an existing vendor credit. |
| DELETE | books/v3/vendorcredits/{id}/comments/{id} | write | vendor-credits | Delete a vendor credit comment. |
| GET | books/v3/vendorcredits/{id}/refunds | read | vendor-credits | List all refunds of an existing vendor credit. |
| POST | books/v3/vendorcredits/{id}/refunds | write | vendor-credits | Refund vendor credit amount. |
| GET | books/v3/vendorcredits/{id}/refunds/{id} | read | vendor-credits | Get refund of a particular vendor credit. |
| PUT | books/v3/vendorcredits/{id}/refunds/{id} | write | vendor-credits | Update the refunded transaction. |
| DELETE | books/v3/vendorcredits/{id}/refunds/{id} | write | vendor-credits | Delete a vendor credit refund. |
| POST | books/v3/vendorcredits/{id}/status/open | write | vendor-credits | Change an existing vendor credit status to open. |
| POST | books/v3/vendorcredits/{id}/status/void | write | vendor-credits | Mark an existing vendor credit as void. |
| POST | books/v3/vendorcredits/{id}/submit | write | vendor-credits | Submit a Vendor credit for approval. |
| GET | books/v3/vendorpayments | read | vendor-payments | List all the payments made to your vendor. |
| POST | books/v3/vendorpayments | write | vendor-payments | Create a payment made to your vendor and you can also apply them to bills either partially or fully. |
| PUT | books/v3/vendorpayments | write | vendor-payments | A custom field will have unique values if it's configured to not accept duplicate values. |
| GET | books/v3/vendorpayments/{id} | read | vendor-payments | Get the details of a vendor payment. |
| PUT | books/v3/vendorpayments/{id} | write | vendor-payments | Update an existing vendor payment. |
| DELETE | books/v3/vendorpayments/{id} | write | vendor-payments | Delete an existing vendor payment. |
| GET | books/v3/vendorpayments/{id}/refunds | read | vendor-payments | List all the refunds pertaining to an existing vendor payment. |
| POST | books/v3/vendorpayments/{id}/refunds | write | vendor-payments | Refund the excess amount paid to the vendor. |
| GET | books/v3/vendorpayments/{id}/refunds/{id} | read | vendor-payments | Obtain details of a particular refund of a vendor payment. |
| PUT | books/v3/vendorpayments/{id}/refunds/{id} | write | vendor-payments | Update the refunded transaction. |
| DELETE | books/v3/vendorpayments/{id}/refunds/{id} | write | vendor-payments | Delete refund pertaining to an existing vendor payment. |
