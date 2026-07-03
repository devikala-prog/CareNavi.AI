import { Bot } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="w-full px-8 py-5 flex justify-between items-center border-b border-slate-200 bg-[bg-white]">
      <div className="flex items-center gap-2">
        <Bot className="text-blue-500" size={30} />
        <h1 className="text-2xl font-bold text-slate-900">
          CareNavi<span className="text-blue-500">.AI</span>
        </h1>
      </div>

      <div className="flex gap-8 text-slate-600">
        <a href="#features" className="hover:text-indigo-600">Features</a>
        <a href="#workflow" className="hover:text-indigo-600">Workflow</a>
        <a href="#about" className="hover:text-indigo-600">About</a>
      </div>

      <button className="bg-indigo-600 px-5 py-2 rounded-xl text-white hover:bg-indigo-700">
        Get Started
      </button>
    </nav>
  );
}