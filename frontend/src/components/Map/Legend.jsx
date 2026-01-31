export default function Legend() {
  return (
    <div className="absolute bottom-6 right-6 z-[9999] bg-white text-black p-3 rounded shadow-lg text-sm">
      <p className="font-bold mb-2">Risk Legend</p>

      <div className="flex items-center gap-2 mb-1">
        <div className="w-4 h-4 bg-red-600 rounded-full"></div>
        <span>Critical – Immediate Evacuation</span>
      </div>

      <div className="flex items-center gap-2 mb-1">
        <div className="w-4 h-4 bg-orange-500 rounded-full"></div>
        <span>High – Prepare Rescue</span>
      </div>

      <div className="flex items-center gap-2">
        <div className="w-4 h-4 bg-yellow-400 rounded-full"></div>
        <span>Moderate – Monitor</span>
      </div>
    </div>
  );
}
