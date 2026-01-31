import helicopterIcon from "../../assets/icons/helicopter.png";
import ambulanceIcon from "../../assets/icons/ambulance.png";
import boatIcon from "../../assets/icons/boat.png";

export default function AlertPanel({ zones, onSelect }) {
  return (
    <div className="w-full md:w-80 h-64 md:h-screen bg-gray-900 text-white p-4 overflow-y-auto">
      <h2 className="text-xl font-bold mb-4">🚨 Live Alerts</h2>

      {zones
        .sort((a, b) => b.risk.risk_score - a.risk.risk_score)
        .map((z, i) => (
          <div
            key={i}
            onClick={() => onSelect(z)}
            className={`p-3 mb-4 rounded cursor-pointer ${z.risk.zone_color === "RED"
                ? "bg-red-600"
                : z.risk.zone_color === "ORANGE"
                  ? "bg-orange-500"
                  : "bg-yellow-400 text-black"
              }`}
          >
            <p className="font-bold">{z.zone}</p>
            <p>Risk: {z.risk.risk_level}</p>

            <div className="flex gap-3 mt-3 items-center">
              <div className="flex items-center gap-1">
                <img src={boatIcon} className="w-5 h-5" />
                <span>{z.resources.boats}</span>
              </div>
              <div className="flex items-center gap-1">
                <img src={ambulanceIcon} className="w-5 h-5" />
                <span>{z.resources.ambulances}</span>
              </div>
              <div className="flex items-center gap-1">
                <img src={helicopterIcon} className="w-5 h-5" />
                <span>{z.resources.helicopters}</span>
              </div>
            </div>

            {/* AI Reasoning */}
            <div className="mt-2 text-xs bg-black/30 p-2 rounded">
              <p className="font-semibold mb-1">🧠 AI Reasoning:</p>
              {z.reasoning.map((r, idx) => (
                <p key={idx}>• {r}</p>
              ))}
            </div>
          </div>
        ))}
    </div>
  );
}
