import { NextRequest, NextResponse } from "next/server";
import { db } from "@/db";
import { categories, methods, resources } from "@/db/schema";
import { eq, asc, inArray } from "drizzle-orm";
import {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  secureErrorResponse,
  methodsQuerySchema,
  SECURITY_CONFIG,
} from "@/lib/security";

export const dynamic = "force-dynamic";

export async function GET(request: NextRequest) {
  // 1. Security enforcement
  const securityResult = await enforceSecurityMiddleware(request, "methods");
  if (!securityResult.allowed) {
    return securityResult.response;
  }
  const { context } = securityResult;

  try {
    // 2. Parse and validate query parameters
    const url = new URL(request.url);
    const rawParams = {
      category: url.searchParams.get("category") || undefined,
      id: url.searchParams.get("id") || undefined,
    };

    const parseResult = methodsQuerySchema.safeParse(rawParams);
    if (!parseResult.success) {
      return wrapSecureResponse(
        secureErrorResponse(SECURITY_CONFIG.errors.validation, 400),
        context,
        "methods"
      );
    }

    const { category: categorySlug, id: methodNumber } = parseResult.data;

    // 3. Single method lookup
    if (methodNumber !== undefined) {
      const result = await db
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
        .where(eq(methods.methodNumber, methodNumber))
        .limit(1);

      if (result.length === 0) {
        return wrapSecureResponse(
          secureErrorResponse(SECURITY_CONFIG.errors.notFound, 404),
          context,
          "methods"
        );
      }

      const methodResources = await db
        .select()
        .from(resources)
        .where(eq(resources.methodId, result[0].methodId));

      const response = NextResponse.json({
        method: { ...result[0], resources: methodResources },
      });
      return wrapSecureResponse(response, context, "methods");
    }

    // 4. Get all methods, optionally filtered by category
    let whereClause;
    if (categorySlug) {
      const cat = await db
        .select({ id: categories.id })
        .from(categories)
        .where(eq(categories.slug, categorySlug))
        .limit(1);

      if (cat.length > 0) {
        whereClause = eq(methods.categoryId, cat[0].id);
      }
    }

    const allMethods = await db
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
      .orderBy(asc(methods.methodNumber));

    // 5. Get resources for methods
    const methodIds = allMethods.map((m) => m.methodId);
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

    // 6. Group resources by method
    const resourcesByMethod = new Map<number, typeof methodResources>();
    for (const res of methodResources) {
      const existing = resourcesByMethod.get(res.methodId) || [];
      existing.push(res);
      resourcesByMethod.set(res.methodId, existing);
    }

    // 7. Combine and return
    const enrichedMethods = allMethods.map((m) => ({
      ...m,
      resources: resourcesByMethod.get(m.methodId) || [],
    }));

    const response = NextResponse.json({ methods: enrichedMethods });
    return wrapSecureResponse(response, context, "methods");
  } catch (error) {
    // Log error internally but don't expose details
    console.error("[METHODS ERROR]", error);
    return wrapSecureResponse(
      secureErrorResponse(SECURITY_CONFIG.errors.generic, 500),
      context,
      "methods"
    );
  }
}
