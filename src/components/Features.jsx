export default function Features() {
  const features = [
    "Multi-Agent Collaboration",
    "Smart Ticket Creation",
    "Sentiment Analysis",
    "Intent Detection",
    "Context Awareness",
    "Analytics Dashboard",
  ];

  return (
    <section id="features" className="bg-slate-50 py-24 text-slate-900">
      <h2 className="text-4xl text-center font-bold mb-16">
        Powerful Features
      </h2>

      <div className="max-w-6xl mx-auto grid md:grid-cols-3 gap-8">
        {features.map((feature) => (
          <div
            key={feature}
            className="bg-white p-8 rounded-2xl border border-slate-200 hover:border-indigo-500 transition"
          >
            <h3 className="text-xl font-semibold">{feature}</h3>
          </div>
        ))}
      </div>
    </section>
  );
}