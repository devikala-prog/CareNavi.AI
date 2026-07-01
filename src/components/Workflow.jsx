export default function Workflow() {
  return (
    <section id="workflow" className="bg-white py-24 text-slate-900">
      <h2 className="text-4xl text-center font-bold mb-12">
        How It Works
      </h2>

      <div className="max-w-5xl mx-auto flex flex-wrap justify-center gap-4 text-center">
        {[
          "Customer",
          "Orchestrator",
          "Intent",
          "Sentiment",
          "Resolution",
          "Ticket",
          "Response",
        ].map((step) => (
          <div
            key={step}
            className="bg-indigo-600 px-5 py-3 rounded-xl font-medium"
          >
            {step}
          </div>
        ))}
      </div>
    </section>
  );
}