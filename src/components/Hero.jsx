import { ArrowRight } from "lucide-react";

export default function Hero() {
  return (
    <section className="min-h-[90vh] flex items-center justify-center bg-slate-50 text-slate-900">
      <div className="max-w-6xl grid md:grid-cols-2 gap-16 items-center">

        <div>
          <h1 className="text-6xl font-extrabold leading-tight">
            Multi-Agent AI
            <span className="text-blue-500"> Customer Support</span>
          </h1>

          <p className="mt-8 text-slate-600 text-lg leading-8">
            CareNavi.AI intelligently routes customer requests through
            specialized AI agents that understand intent, detect emotions,
            generate solutions, and automate support tickets.
          </p>

          <div className="mt-10 flex gap-5">
            <button className="bg-blue-600 px-6 py-3 rounded-xl flex items-center gap-2 hover:bg-blue-700">
              Start Chat
              <ArrowRight size={18} />
            </button>

            <button className="border border-gray-600 px-6 py-3 rounded-xl">
              Live Demo
            </button>
          </div>
        </div>

        <div className="bg-white rounded-3xl p-8 border border-slate-200 shadow-x1 p-8">
          <h2 className="text-2xl mb-6 font-bold">
            🤖 AI Agent Activity
          </h2>

          <div className="space-y-5">

            <div className="flex justify-between">
              <span>🧠 Intent Agent</span>
              <span className="text-green-400">Billing Issue ✔</span>
            </div>

            <div className="flex justify-between">
              <span>😊 Sentiment Agent</span>
              <span className="text-yellow-400">Frustrated</span>
            </div>

            <div className="flex justify-between">
              <span>🛠 Resolution Agent</span>
              <span className="text-blue-400">Refund Initiated</span>
            </div>

            <div className="flex justify-between">
              <span>🎫 Ticket Agent</span>
              <span className="text-green-400">Created</span>
            </div>

          </div>
        </div>

      </div>
    </section>
  );
}