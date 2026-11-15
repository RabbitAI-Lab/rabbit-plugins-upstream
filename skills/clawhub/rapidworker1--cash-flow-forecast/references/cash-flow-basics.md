# US payment timing and payroll rules that change a forecast

Reference for the Cash Flow Forecast skill. Every limit and rule below is a US-facing constraint the workflow has to respect.

## Payment timing

- ACH: usually 1 to 3 business days to settle, so plan payroll against the slow end.
- Wire: same day or next business day, and the fee belongs in the outflow column.
- Amex and Mastercard: settlement typically 1 to 3 business days after the sale.
- Checks: add mail time and clearing time before you count the cash as available.

## US payroll and tax outflows

- Payroll taxes are deposited on the payroll schedule, and late deposits are penalized at 2% to 5% plus interest.
- Federal estimated tax payments land on the standard dates and are not optional once the threshold is met.
- State unemployment and state withholding payments have their own due dates.
- Reconcile the deposit dates to the bank statement, not to the payroll register.

## Forecast hygiene

- Use cash movement, not accrual profit, in the forecast.
- Write down the assumptions that would break the plan if they are wrong.
- Rerun the grid every week with the latest bank balance.
- Keep the low case usable: if the business cannot run on it, the plan needs another look.
