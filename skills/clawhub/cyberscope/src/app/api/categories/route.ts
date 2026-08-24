import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { categories, methods } from "@/db/schema";
import { eq, sql, asc } from "drizzle-orm";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  // 1. Security enforcement
  const securityResult = await enforceSecurityMiddleware(request, "categories");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // 2. Execute query with parameterized statements
    const result = await db
      .select({
        id: categories.id,
        numeral: categories.numeral,
        name: categories.name,
        slug: categories.slug,
        description: categories.description,
        sortOrder: categories.sortOrder,
        methodCount: sql<number>`count(${methods.id})::int`,
      })
      .from(categories)
      .leftJoin(methods, eq(categories.id, methods.categoryId))
      .groupBy(categories.id)
      .orderBy(asc(categories.sortOrder));

    // 3. Return secure response
    const response = NextResponse.json({ categories: result });
    return wrapSecureResponse(response, context, "categories");
  } catch (error) {
    // Log error internally but don't expose details
    console.error("[CATEGORIES ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "categories"
    );
  }
}
