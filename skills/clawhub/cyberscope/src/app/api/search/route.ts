import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { categories, methods, resources, searchHistory } from "@/db/schema";
import { eq, ilike, or, and, inArray, asc, sql } from "drizzle-orm";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  searchQuerySchema,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  // 1. Security enforcement
  const securityResult = await enforceSecurityMiddleware(request, "search");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // 2. Parse and validate query parameters
    const url = new URL(request.url);
    const rawParams = {
      q: url.searchParams.get("q") || "",
      category: url.searchParams.get("category") || "",
      page: url.searchParams.get("page") || "1",
      limit: url.searchParams.get("limit") || "20",
    };

    // Validate with Zod schema
    const parseResult = searchQuerySchema.safeParse(rawParams);
    if (!parseResult.success) {
      return wrapSecureResponse(
        secureErrorResponse(SECURITY_CONFIG.errors.validation, 400),
        context,
        "search"
      );
    }

    const { q: query, category, page, limit } = parseResult.data;
    const offset = (page - 1) * limit;

    // 3. Empty query check
    if (!query && !category) {
      const response = NextResponse.json({ 
        results: [], 
        total: 0, 
        page, 
        limit,
        totalPages: 0,
      });
      return wrapSecureResponse(response, context, "search");
    }

    // 4. Build search conditions with parameterized queries (Drizzle handles this)
    const conditions: ReturnType<typeof ilike>[] = [];

    if (query) {
      // Drizzle ORM automatically parameterizes - safe from SQL injection
      const searchTerm = `%${query}%`;
      conditions.push(
        ilike(methods.title, searchTerm),
        ilike(methods.description, searchTerm)
      );
    }

    // 5. Get category ID if specified
    let categoryId: number | null = null;
    if (category) {
      const cat = await db
        .select({ id: categories.id })
        .from(categories)
        .where(eq(categories.slug, category))
        .limit(1);
      if (cat.length > 0) {
        categoryId = cat[0].id;
      }
    }

    // 6. Build where clause
    let whereClause;
    if (query && categoryId) {
      whereClause = and(eq(methods.categoryId, categoryId), or(...conditions));
    } else if (query) {
      whereClause = or(...conditions);
    } else if (categoryId) {
      whereClause = eq(methods.categoryId, categoryId);
    }

    // 7. Execute search query
    const results = await db
      .select({
        methodId: methods.id,
        methodNumber: methods.methodNumber,
        title: methods.title,
        description: methods.description,
        keywords: methods.keywords,
        categoryId: categories.id,
        categoryName: categories.name,
        categoryNumeral: categories.numeral,
        categorySlug: categories.slug,
      })
      .from(methods)
      .innerJoin(categories, eq(methods.categoryId, categories.id))
      .where(whereClause)
      .orderBy(asc(methods.methodNumber))
      .limit(limit)
      .offset(offset);

    // 8. Get total count
    const countResult = await db
      .select({ count: sql<number>`count(*)::int` })
      .from(methods)
      .innerJoin(categories, eq(methods.categoryId, categories.id))
      .where(whereClause);

    const total = countResult[0]?.count || 0;

    // 9. Get resources for methods
    const methodIds = results.map((r) => r.methodId);
    let methodResources: Array<{
      id: number;
      methodId: number;
      title: string;
      url: string;
      source: string | null;
      resourceType: string;
      description: string | null;
    }> = [];

    if (methodIds.length > 0) {
      methodResources = await db
        .select()
        .from(resources)
        .where(inArray(resources.methodId, methodIds));
    }

    // 10. Group resources by method
    const resourcesByMethod = new Map<number, typeof methodResources>();
    for (const res of methodResources) {
      const existing = resourcesByMethod.get(res.methodId) || [];
      existing.push(res);
      resourcesByMethod.set(res.methodId, existing);
    }

    // 11. Combine results
    const enrichedResults = results.map((r) => ({
      ...r,
      resources: resourcesByMethod.get(r.methodId) || [],
    }));

    // 12. Log search (async, don't wait)
    if (query) {
      db.insert(searchHistory)
        .values({
          query: query.slice(0, 200), // Limit stored query length
          resultsCount: total,
          categoryFilter: category || null,
        })
        .catch(() => {
          // Silently fail - search logging is non-critical
        });
    }

    // 13. Return secure response
    const response = NextResponse.json({
      results: enrichedResults,
      total,
      page,
      limit,
      totalPages: Math.ceil(total / limit),
    });

    return wrapSecureResponse(response, context, "search");
  } catch (error) {
    // Log error internally but don't expose details
    console.error("[SEARCH ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "search"
    );
  }
}
