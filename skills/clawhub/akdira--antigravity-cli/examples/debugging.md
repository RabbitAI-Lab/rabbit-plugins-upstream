# Example: Debugging

## Scenario
Investigate and fix a bug where function returns NaN.

## Command

```bash
agy -p "Debug this issue:

**Problem:** The function \`calculateTotal()\` in \`src/cart.js\` returns \`NaN\` when the cart is empty.

**Expected behavior:** Should return 0 for empty cart.

**Current behavior:** Returns NaN, causing checkout to fail.

**Steps to reproduce:**
1. Create empty cart
2. Call calculateTotal()
3. Observe NaN result

**Code context:**
\`\`\`javascript
function calculateTotal(cart) {
  return cart.items.reduce((sum, item) => sum + item.price * item.quantity);
}
\`\`\`

Please:
1. Identify the root cause
2. Explain why it happens
3. Provide a fix
4. Add proper null/edge case handling
5. Write unit tests to prevent regression"
```

## Expected Output

```markdown
## Root Cause Analysis

The issue occurs because `Array.reduce()` without an initial value returns the first element when array has items, but throws error/returns undefined for empty arrays.

When `cart.items` is empty:
- `reduce()` has no initial value
- Returns undefined
- undefined + number = NaN

## Fix

\`\`\`javascript
function calculateTotal(cart) {
  if (!cart || !cart.items || cart.items.length === 0) {
    return 0;
  }
  
  return cart.items.reduce((sum, item) => {
    const price = Number(item.price) || 0;
    const quantity = Number(item.quantity) || 0;
    return sum + (price * quantity);
  }, 0); // Initial value prevents undefined
}
\`\`\`

## Unit Tests

\`\`\`javascript
describe('calculateTotal', () => {
  test('returns 0 for empty cart', () => {
    expect(calculateTotal({ items: [] })).toBe(0);
  });
  
  test('returns 0 for null cart', () => {
    expect(calculateTotal(null)).toBe(0);
  });
  
  test('handles missing price/quantity', () => {
    const cart = { items: [{ price: null, quantity: 2 }] };
    expect(calculateTotal(cart)).toBe(0);
  });
  
  test('calculates correct total', () => {
    const cart = { items: [
      { price: 10, quantity: 2 },
      { price: 5, quantity: 3 }
    ]};
    expect(calculateTotal(cart)).toBe(35);
  });
});
\`\`\`
```

## Tips

- Provide clear problem description
- Include steps to reproduce
- Share relevant code context
- Use `--effort high` for complex bugs
- Ask for unit tests to prevent regression
