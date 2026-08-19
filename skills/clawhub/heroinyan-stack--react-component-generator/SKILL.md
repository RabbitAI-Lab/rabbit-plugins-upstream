---
name: react-component-generator-design-systems
version: "1.0.0"
category: frontend
tags:
  - react
  - components
  - design-system
  - tailwind
  - typescript
  - accessibility
  - shadcn
  - radix
  - ui
model: claude-sonnet-4-20250514
trigger_keywords:
  - React component
  - UI component
  - design system
  - component library
  - accessible component
  - Tailwind React
  - shadcn component
  - React TypeScript
  - form component
  - table component
pricing: "$7.99 one-time"
---

# React Component Generator with Design Systems

> **Generate production-ready React components that match your design system.** Auto-detects your UI library (shadcn/ui, MUI, Chakra, Tailwind), generates accessible, TypeScript-typed components with proper variants, forwardRef, and Storybook stories.

## Why This Skill Exists

AI-generated React components often ignore design systems, lack accessibility, miss TypeScript types, and don't follow React 19 patterns. This skill reads your project's existing components and design tokens to generate components that look like they belong in your codebase.

## When to Activate

Activate when the user:
- Asks to create a React component
- Mentions design system, UI library, or component library
- Needs form components, data tables, modals, or complex UI
- Says "build a component for..." or "generate a UI component"

## Workflow

### Step 1: Detect Design System

Scan the project for:
- **UI Library**: shadcn/ui, MUI, Chakra UI, Ant Design, Mantine, Radix UI
- **Styling**: Tailwind CSS, CSS Modules, Styled Components, vanilla-extract
- **TypeScript**: check tsconfig.json for strict mode, path aliases
- **Component patterns**: forwardRef usage, `cn()` utility, variant patterns
- **Design tokens**: theme config, CSS variables, Tailwind config
- **Form library**: react-hook-form, Formik, react-final-form
- **Animation**: framer-motion, react-spring, CSS transitions
- **Icon library**: lucide-react, react-icons, heroicons

### Step 2: Generate Component

Based on detected patterns, generate a complete component:

```tsx
"use client";

import * as React from "react";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";
import { Loader2, ChevronDown } from "lucide-react";

// ===== Variant Definitions =====
const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-md text-sm font-medium transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50",
  {
    variants: {
      variant: {
        default: "bg-primary text-primary-foreground hover:bg-primary/90",
        destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
        outline: "border border-input bg-background hover:bg-accent hover:text-accent-foreground",
        secondary: "bg-secondary text-secondary-foreground hover:bg-secondary/80",
        ghost: "hover:bg-accent hover:text-accent-foreground",
        link: "text-primary underline-offset-4 hover:underline",
      },
      size: {
        default: "h-10 px-4 py-2",
        sm: "h-9 rounded-md px-3",
        lg: "h-11 rounded-md px-8",
        icon: "h-10 w-10",
      },
    },
    defaultVariants: {
      variant: "default",
      size: "default",
    },
  }
);

// ===== Props Interface =====
export interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  loading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

// ===== Component =====
const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, loading, leftIcon, rightIcon, children, disabled, ...props }, ref) => {
    return (
      <button
        className={cn(buttonVariants({ variant, size, className }))}
        ref={ref}
        disabled={disabled || loading}
        aria-busy={loading}
        {...props}
      >
        {loading && <Loader2 className="h-4 w-4 animate-spin" aria-hidden="true" />}
        {!loading && leftIcon && <span className="inline-flex">{leftIcon}</span>}
        {children}
        {!loading && rightIcon && <span className="inline-flex">{rightIcon}</span>}
      </button>
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };
export type { ButtonProps };
```

### Step 3: Generate Component Variants for Common Patterns

#### Data Table Component
```tsx
// Generated with: sorting, filtering, pagination, row selection
export function DataTable<TData, TValue>({
  columns,
  data,
  pagination,
}: DataTableProps<TData, TValue>) {
  // ... full implementation with TanStack Table
}
```

#### Form Field Component
```tsx
// Generated with: label, error display, react-hook-form integration
export function FormField<TFieldValues extends FieldValues>({
  name,
  label,
  description,
  required,
  render,
}: FormFieldProps<TFieldValues>) {
  // ... full implementation with accessibility
}
```

#### Modal/Dialog Component
```tsx
// Generated with: focus trap, escape to close, portal, animation
export function Modal({ trigger, children, title, description }: ModalProps) {
  // ... Radix UI Dialog with framer-motion animation
}
```

### Step 4: Generate Storybook Story

```tsx
import type { Meta, StoryObj } from "@storybook/react";
import { Button } from "./Button";

const meta = {
  title: "UI/Button",
  component: Button,
  parameters: { layout: "centered" },
  tags: ["autodocs"],
  argTypes: {
    variant: {
      control: "select",
      options: ["default", "destructive", "outline", "secondary", "ghost", "link"],
    },
    size: { control: "select", options: ["default", "sm", "lg", "icon"] },
  },
} satisfies Meta<typeof Button>;

export default meta;
type Story = StoryObj<typeof meta>;

export const Default: Story = { args: { children: "Button" } };
export const Destructive: Story = { args: { children: "Delete", variant: "destructive" } };
export const Loading: Story = { args: { children: "Saving...", loading: true } };
export const WithIcon: Story = {
  args: { children: "Download", leftIcon: <DownloadIcon /> },
};
export const Disabled: Story = { args: { children: "Disabled", disabled: true } };
```

### Step 5: Generate Tests

```tsx
import { render, screen, fireEvent } from "@testing-library/react";
import { Button } from "./Button";

describe("Button", () => {
  it("renders children correctly", () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole("button", { name: /click me/i })).toBeInTheDocument();
  });

  it("handles onClick events", () => {
    const handleClick = jest.fn();
    render(<Button onClick={handleClick}>Click</Button>);
    fireEvent.click(screen.getByRole("button"));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it("disables when loading is true", () => {
    render(<Button loading>Saving</Button>);
    expect(screen.getByRole("button")).toBeDisabled();
    expect(screen.getByRole("button")).toHaveAttribute("aria-busy", "true");
  });

  it("applies variant classes correctly", () => {
    render(<Button variant="destructive">Delete</Button>);
    expect(screen.getByRole("button")).toHaveClass("bg-destructive");
  });
});
```

## Output Constraints

- All components must use `forwardRef` (React 19 compatible)
- All components must include proper TypeScript types (no `any`)
- All interactive elements must be keyboard accessible (tabindex, aria attributes)
- All components must support `className` prop for customization
- Variants must use `cva` (class-variance-authority) pattern
- Storybook stories must cover all variants and states
- Tests must cover: rendering, user interaction, disabled/loading states, accessibility
- Must match existing project's import paths (`@/components`, `@/lib/utils`)

## What This Skill Does NOT Do

- Does not install dependencies (lists what to install)
- Does not modify existing components (generates new ones)
- Does not generate CSS-in-JS for styled-components projects (uses detected styling approach)
- Does not handle server components vs client components automatically (defaults to "use client")
