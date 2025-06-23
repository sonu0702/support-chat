import { NextRequest, NextResponse } from 'next/server';

export async function POST(req: NextRequest) {
  const { message } = await req.json();
  console.log("POST response",process.env.NEXT_BASE_URL);
  const response = await fetch(`${process.env.NEXT_BASE_URL}/ask`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ question: message }),
  });

  if (!response.ok) {
    return NextResponse.json({ error: 'Something went wrong' }, { status: 500 });
  }
  const data = await response.json();
  return NextResponse.json({ reply: data?.answer });
}
