import os, re, glob, shutil

SITE_DIR = "/home/roman/portfolio-gallery-sites"
PRO_DIR = "/home/roman/gallery-sites-pro"

# -------------------------------------------------------------
# 1. GLOWUP: VIP Atelier Salon Reservation System & Live Calendar
# -------------------------------------------------------------
def update_glowup():
    path = os.path.join(SITE_DIR, "glowup/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* GlowUp Advanced Reservation Wizard Styles */
.res-step { display: none; }
.res-step.active { display: block; animation: fadeIn 0.3s ease-out; }
.res-progress { display: flex; justify-content: space-between; margin-bottom: 20px; position: relative; }
.res-progress::before { content: ''; position: absolute; top: 50%; left: 0; right: 0; height: 2px; background: var(--border); z-index: 1; transform: translateY(-50%); }
.res-progress-step { width: 32px; height: 32px; border-radius: 50%; background: var(--surface); border: 2px solid var(--border); display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; color: var(--text-muted); position: relative; z-index: 2; transition: all 0.3s ease; }
.res-progress-step.active { background: var(--accent); border-color: var(--accent); color: #fff; box-shadow: 0 0 12px rgba(224, 122, 95, 0.4); }
.res-progress-step.completed { background: #10b981; border-color: #10b981; color: #fff; }

.stylist-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin: 15px 0; }
@media (max-width: 600px) { .stylist-grid { grid-template-columns: 1fr; } }
.stylist-card { border: 2px solid var(--border); border-radius: 12px; padding: 12px; text-align: center; cursor: pointer; transition: all 0.2s ease; background: var(--surface); }
.stylist-card:hover { border-color: var(--accent); transform: translateY(-2px); }
.stylist-card.selected { border-color: var(--accent); background: rgba(224, 122, 95, 0.08); box-shadow: 0 4px 14px rgba(224, 122, 95, 0.15); }
.stylist-img { width: 52px; height: 52px; border-radius: 50%; object-fit: cover; margin: 0 auto 8px; }
.stylist-name { font-weight: 700; font-size: 14px; color: var(--text); }
.stylist-title { font-size: 11px; color: var(--text-muted); }

.time-slot-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 10px; }
@media (max-width: 500px) { .time-slot-grid { grid-template-columns: repeat(2, 1fr); } }
.time-slot-btn { padding: 8px; border-radius: 8px; border: 1px solid var(--border); background: var(--surface); color: var(--text); font-size: 13px; font-weight: 600; cursor: pointer; text-align: center; transition: all 0.2s ease; }
.time-slot-btn:hover { border-color: var(--accent); }
.time-slot-btn.selected { background: var(--accent); color: #fff; border-color: var(--accent); }
.time-slot-btn.disabled { opacity: 0.4; cursor: not-allowed; text-decoration: line-through; }

.booking-confirm-card { background: rgba(224, 122, 95, 0.06); border: 1px dashed var(--accent); border-radius: 12px; padding: 16px; margin: 15px 0; }
.booking-confirm-row { display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 13px; }
.booking-confirm-label { color: var(--text-muted); }
.booking-confirm-val { font-weight: 700; color: var(--text); }
"""
    if "/* GlowUp Advanced Reservation Wizard Styles */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- Multi-Step Atelier Reservation Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Atelier VIP Reservation System</h3>
                    <p class="modal-sub">Live Real-Time Appointment & Specialist Dispatch</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>

            <div class="res-progress">
                <div class="res-progress-step active" id="prog1">1</div>
                <div class="res-progress-step" id="prog2">2</div>
                <div class="res-progress-step" id="prog3">3</div>
                <div class="res-progress-step" id="prog4">✓</div>
            </div>

            <!-- Step 1: Select Stylist & Ritual -->
            <div class="res-step active" id="step1">
                <label class="form-label" style="font-weight:700;">Select Your Master Artisan</label>
                <div class="stylist-grid">
                    <div class="stylist-card selected" onclick="selectStylist(this, 'Elena Rostova', 'Creative Color Director')">
                        <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=150&q=80" alt="Elena" class="stylist-img">
                        <div class="stylist-name">Elena Rostova</div>
                        <div class="stylist-title">Color Director</div>
                    </div>
                    <div class="stylist-card" onclick="selectStylist(this, 'Sophie Laurent', 'Parisian Hair Couturière')">
                        <img src="https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=150&q=80" alt="Sophie" class="stylist-img">
                        <div class="stylist-name">Sophie Laurent</div>
                        <div class="stylist-title">Hair Couturière</div>
                    </div>
                    <div class="stylist-card" onclick="selectStylist(this, 'Nino Kalandadze', 'Senior Dermal Specialist')">
                        <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=150&q=80" alt="Nino" class="stylist-img">
                        <div class="stylist-name">Nino Kalandadze</div>
                        <div class="stylist-title">Skin Specialist</div>
                    </div>
                </div>

                <div class="form-group" style="margin-top:15px;">
                    <label class="form-label">Chosen Atelier Service / Ritual</label>
                    <input type="text" class="form-input" id="modalServiceInput" value="French Balayage & Olaplex Glaze" placeholder="Custom Service or Ritual">
                </div>
                <button type="button" class="modal-submit-btn" onclick="goToStep(2)">Continue to Date & Time Selection ➔</button>
            </div>

            <!-- Step 2: Date & Time Picker -->
            <div class="res-step" id="step2">
                <div class="form-group">
                    <label class="form-label">Preferred Date</label>
                    <input type="date" class="form-input" id="resDate" min="2026-08-20" value="2026-08-21">
                </div>
                <label class="form-label">Available VIP Slots (Live Updated)</label>
                <div class="time-slot-grid">
                    <div class="time-slot-btn" onclick="selectSlot(this)">10:30 AM</div>
                    <div class="time-slot-btn selected" onclick="selectSlot(this)">12:00 PM</div>
                    <div class="time-slot-btn" onclick="selectSlot(this)">02:15 PM</div>
                    <div class="time-slot-btn disabled">04:00 PM (Booked)</div>
                    <div class="time-slot-btn" onclick="selectSlot(this)">05:30 PM</div>
                    <div class="time-slot-btn" onclick="selectSlot(this)">07:00 PM</div>
                    <div class="time-slot-btn" onclick="selectSlot(this)">08:15 PM</div>
                </div>
                <div style="display:flex; gap:10px; margin-top:20px;">
                    <button type="button" class="btn" style="background:var(--surface); border:1px solid var(--border); flex:1;" onclick="goToStep(1)">← Back</button>
                    <button type="button" class="modal-submit-btn" style="flex:2;" onclick="goToStep(3)">Enter Guest Details ➔</button>
                </div>
            </div>

            <!-- Step 3: Guest Info & Confirm -->
            <div class="res-step" id="step3">
                <form onsubmit="handleReservationSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Full Name</label>
                        <input type="text" class="form-input" id="guestName" placeholder="e.g. Tamar Dadiani" required value="Tamar Dadiani">
                    </div>
                    <div class="form-group">
                        <label class="form-label">WhatsApp / Phone</label>
                        <input type="tel" class="form-input" id="guestPhone" placeholder="+995 599 00 00 00" required value="+995 599 12 34 56">
                    </div>
                    
                    <div class="booking-confirm-card">
                        <div class="booking-confirm-row">
                            <span class="booking-confirm-label">Artisan:</span>
                            <span class="booking-confirm-val" id="summaryStylist">Elena Rostova</span>
                        </div>
                        <div class="booking-confirm-row">
                            <span class="booking-confirm-label">Service:</span>
                            <span class="booking-confirm-val" id="summaryService">French Balayage</span>
                        </div>
                        <div class="booking-confirm-row">
                            <span class="booking-confirm-label">Schedule:</span>
                            <span class="booking-confirm-val" id="summaryTime">Aug 21, 2026 at 12:00 PM</span>
                        </div>
                        <div class="booking-confirm-row" style="border-top:1px solid rgba(224,122,95,0.2); padding-top:6px; margin-top:6px;">
                            <span class="booking-confirm-label">Booking Status:</span>
                            <span class="booking-confirm-val" style="color:#10b981;">⚡ Instant VIP Slot Reserved</span>
                        </div>
                    </div>
                    
                    <div style="display:flex; gap:10px; margin-top:15px;">
                        <button type="button" class="btn" style="background:var(--surface); border:1px solid var(--border); flex:1;" onclick="goToStep(2)">← Back</button>
                        <button type="submit" class="modal-submit-btn" style="flex:2;">Confirm Atelier Appointment ➔</button>
                    </div>
                </form>
            </div>

            <!-- Step 4: Success Instant Confirmation -->
            <div class="res-step" id="step4" style="text-align:center; padding: 20px 0;">
                <div style="width:64px; height:64px; border-radius:50%; background:rgba(16,185,129,0.15); color:#10b981; font-size:32px; display:flex; align-items:center; justify-content:center; margin: 0 auto 15px;">✓</div>
                <h3 style="font-size:22px; margin-bottom:8px;">Reservation Confirmed!</h3>
                <p style="color:var(--text-muted); font-size:14px; margin-bottom:20px;">A VIP concierge confirmation SMS and calendar invite has been simulated to your device.</p>
                <div class="booking-confirm-card" style="text-align:left;">
                    <div class="booking-confirm-row">
                        <span class="booking-confirm-label">Booking Reference:</span>
                        <span class="booking-confirm-val" id="resRef">#GLOW-92841</span>
                    </div>
                    <div class="booking-confirm-row">
                        <span class="booking-confirm-label">Client:</span>
                        <span class="booking-confirm-val" id="finalGuestName">Tamar Dadiani</span>
                    </div>
                    <div class="booking-confirm-row">
                        <span class="booking-confirm-label">Location:</span>
                        <span class="booking-confirm-val">Abashidze St. 34, Vake, Tbilisi</span>
                    </div>
                </div>
                <button type="button" class="btn btn-primary" style="width:100%; margin-top:15px;" onclick="closeBookingModal()">Done & Back to Showcase</button>
            </div>
        </div>
    </div>"""

    # Replace modal
    pattern = r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>'
    if re.search(pattern, html, re.S):
        html = re.sub(pattern, modal_html, html, flags=re.S)

    js_code = """
let currentStylist = "Elena Rostova";
let currentSlot = "12:00 PM";

function selectStylist(elem, name, title) {
    document.querySelectorAll('.stylist-card').forEach(c => c.classList.remove('selected'));
    elem.classList.add('selected');
    currentStylist = name;
}

function selectSlot(elem) {
    if (elem.classList.contains('disabled')) return;
    document.querySelectorAll('.time-slot-btn').forEach(b => b.classList.remove('selected'));
    elem.classList.add('selected');
    currentSlot = elem.textContent.trim();
}

function goToStep(step) {
    document.querySelectorAll('.res-step').forEach(s => s.classList.remove('active'));
    document.getElementById('step' + step).classList.add('active');
    
    for (let i = 1; i <= 4; i++) {
        const p = document.getElementById('prog' + i);
        if (i < step) { p.className = 'res-progress-step completed'; }
        else if (i === step) { p.className = 'res-progress-step active'; }
        else { p.className = 'res-progress-step'; }
    }
    
    if (step === 3) {
        document.getElementById('summaryStylist').textContent = currentStylist;
        document.getElementById('summaryService').textContent = document.getElementById('modalServiceInput').value || 'Custom Ritual';
        const d = document.getElementById('resDate').value;
        document.getElementById('summaryTime').textContent = (d ? d : 'Aug 21, 2026') + ' at ' + currentSlot;
    }
}

function handleReservationSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('guestName').value;
    document.getElementById('finalGuestName').textContent = name;
    document.getElementById('resRef').textContent = '#GLOW-' + Math.floor(10000 + Math.random() * 90000);
    goToStep(4);
}

function openBookingModal(serviceName) {
    if (serviceName) {
        document.getElementById('modalServiceInput').value = serviceName;
    }
    goToStep(1);
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "let currentStylist =" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ GlowUp VIP Reservation system installed.")

# -------------------------------------------------------------
# 2. AQUAFIX: Live Technician GPS Dispatch Simulator
# -------------------------------------------------------------
def update_aquafix():
    path = os.path.join(SITE_DIR, "aquafix/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* AquaFix Dispatch Simulator Styles */
.dispatch-map-card { background: #0b1522; border-radius: 12px; border: 1px solid var(--border); overflow: hidden; margin: 15px 0; position: relative; padding: 15px; }
.radar-scan { position: absolute; top: 50%; left: 50%; width: 140px; height: 140px; border-radius: 50%; border: 2px solid rgba(0, 180, 216, 0.4); transform: translate(-50%, -50%); animation: pulseRadar 2s infinite ease-out; pointer-events: none; }
@keyframes pulseRadar { 0% { width: 20px; height: 20px; opacity: 1; } 100% { width: 220px; height: 220px; opacity: 0; } }
.tech-pin { display: flex; align-items: center; gap: 10px; background: rgba(0, 180, 216, 0.15); border: 1px solid var(--accent); padding: 8px 12px; border-radius: 30px; font-size: 13px; font-weight: 700; color: #fff; width: fit-content; margin: 10px auto; }
.eta-live-badge { display: inline-block; background: #10b981; color: #fff; font-size: 11px; padding: 3px 8px; border-radius: 12px; font-weight: 700; }
"""
    if "/* AquaFix Dispatch Simulator Styles */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- AquaFix Emergency Dispatch Simulator Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 580px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Emergency Rapid Response Dispatch</h3>
                    <p class="modal-sub">24/7 Priority Water Engineering & Mobile Van Unit</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="dispatchFormStep">
                <form onsubmit="handleAquaDispatch(event)">
                    <div class="form-group">
                        <label class="form-label">Client Name & Property</label>
                        <input type="text" class="form-input" id="aqName" placeholder="e.g. Giorgi Mikeladze" value="Giorgi Mikeladze" required>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Tbilisi District / Exact Address</label>
                        <select class="form-input" id="aqDistrict">
                            <option value="Vake (Chavchavadze Ave)">Vake (Chavchavadze Ave)</option>
                            <option value="Saburtalo (Pekini Ave)">Saburtalo (Pekini Ave)</option>
                            <option value="Mtatsminda / Rustaveli">Mtatsminda / Rustaveli</option>
                            <option value="Didi Dighomi">Didi Dighomi</option>
                            <option value="Isani / Samgori">Isani / Samgori</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">Plumbing Issue / System</label>
                        <input type="text" class="form-input" id="modalServiceInput" value="High-Pressure Pipe Burst & Water Shutdown" placeholder="Service required">
                    </div>
                    <div style="background:rgba(0,180,216,0.08); border-left:3px solid var(--accent); padding:10px 14px; border-radius:6px; font-size:13px; margin-bottom:15px;">
                        🚨 <strong>Rapid Master Dispatch:</strong> Nearest master technician is standing by on active patrol.
                    </div>
                    <button type="submit" class="modal-submit-btn">🚀 Dispatch Nearest Mobile Unit (Simulate) ➔</button>
                </form>
            </div>

            <div id="dispatchTrackStep" style="display:none; text-align:center;">
                <div class="dispatch-map-card">
                    <div class="radar-scan"></div>
                    <div style="font-size:36px; margin-bottom:5px;">🚐💨</div>
                    <div class="tech-pin">
                        <span class="eta-live-badge">ON ROUTE</span>
                        <span>Master David G. (#VAN-04)</span>
                    </div>
                    <div style="font-size:13px; color:#94a3b8; margin-top:8px;" id="dispatchStatusText">Navigating via Kazbegi Ave • Distance: 2.3 km</div>
                </div>

                <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:15px 0;">
                    <div style="background:rgba(255,255,255,0.04); border:1px solid var(--border); padding:12px; border-radius:10px; text-align:left;">
                        <div style="font-size:11px; color:var(--text-muted);">ESTIMATED ARRIVAL</div>
                        <div style="font-size:18px; font-weight:800; color:var(--accent);" id="etaTimer">14 MINS</div>
                    </div>
                    <div style="background:rgba(255,255,255,0.04); border:1px solid var(--border); padding:12px; border-radius:10px; text-align:left;">
                        <div style="font-size:11px; color:var(--text-muted);">TRUCK TELEMETRY</div>
                        <div style="font-size:18px; font-weight:800; color:#10b981;">TOOLS LOADED</div>
                    </div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Confirm & Close Dispatch View</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleAquaDispatch(e) {
    e.preventDefault();
    document.getElementById('dispatchFormStep').style.display = 'none';
    document.getElementById('dispatchTrackStep').style.display = 'block';
    
    const district = document.getElementById('aqDistrict').value;
    document.getElementById('dispatchStatusText').textContent = 'Navigating towards ' + district + ' • Master Unit dispatched';
    
    let seconds = 14;
    const timerElem = document.getElementById('etaTimer');
    const interval = setInterval(() => {
        if (seconds > 3) {
            seconds--;
            timerElem.textContent = seconds + ' MINS';
        } else {
            clearInterval(interval);
        }
    }, 1200);
}

function openBookingModal(serviceName) {
    if (serviceName) {
        document.getElementById('modalServiceInput').value = serviceName;
    }
    document.getElementById('dispatchFormStep').style.display = 'block';
    document.getElementById('dispatchTrackStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleAquaDispatch(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ AquaFix Dispatch tracking simulation installed.")

# -------------------------------------------------------------
# 3. AUTOPRO: Dyno Run & ECU Calibration Performance Simulator
# -------------------------------------------------------------
def update_autopro():
    path = os.path.join(SITE_DIR, "autopro/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* AutoPro Dyno Simulator */
.dyno-screen { background: #06080d; border: 1px solid #ff3e3e; border-radius: 12px; padding: 15px; margin: 15px 0; text-align: center; }
.dyno-gauges { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-top: 12px; }
.gauge-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,62,62,0.2); border-radius: 8px; padding: 10px; }
.gauge-val { font-size: 22px; font-weight: 900; color: #ff3e3e; font-family: 'Chakra Petch', sans-serif; }
.gauge-label { font-size: 10px; color: #94a3b8; text-transform: uppercase; }
.dyno-bar-wrap { height: 12px; background: #161a23; border-radius: 6px; overflow: hidden; margin-top: 10px; }
.dyno-bar-fill { height: 100%; width: 0%; background: linear-gradient(90deg, #ff8c00, #ff3e3e); transition: width 0.1s linear; }
"""
    if "/* AutoPro Dyno Simulator */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- AutoPro ECU Remap & Dyno Booking Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Tuning Bay & ECU Calibration Booking</h3>
                    <p class="modal-sub">Dyno-Cell Reservation & Telemetry Logging</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="dynoBookingStep">
                <form onsubmit="startDynoSimulation(event)">
                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Vehicle Make & Model</label>
                            <input type="text" class="form-input" id="carModel" value="BMW M3 Competition (G80)" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">ECU Software Level</label>
                            <select class="form-input" id="tuningStage">
                                <option value="Stage 1 Custom (+70 HP / +110 Nm)">Stage 1 Custom (+70 HP / +110 Nm)</option>
                                <option value="Stage 2 Track (Downpipe + Catless, +125 HP)">Stage 2 Track (Downpipe, +125 HP)</option>
                                <option value="TCU Transmission Flash (xHP)">TCU Transmission Flash (xHP)</option>
                            </select>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Preferred Date & Dyno Slot</label>
                        <input type="datetime-local" class="form-input" id="dynoDate" value="2026-08-22T14:30">
                    </div>

                    <div class="form-group">
                        <label class="form-label">Pilot / Owner Contact</label>
                        <input type="tel" class="form-input" id="driverPhone" value="+995 577 88 99 00" required>
                    </div>

                    <button type="submit" class="modal-submit-btn">🔥 Run Real-Time Dyno Telemetry Simulation ➔</button>
                </form>
            </div>

            <div id="dynoRunStep" style="display:none;">
                <div class="dyno-screen">
                    <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:700; color:#ff3e3e;">
                        <span>4WD SYNCHRONIZED DYNO CELL</span>
                        <span id="dynoStatus">RUNNING 4TH GEAR PULL...</span>
                    </div>
                    
                    <div class="dyno-bar-wrap">
                        <div class="dyno-bar-fill" id="dynoRpmBar"></div>
                    </div>

                    <div class="dyno-gauges">
                        <div class="gauge-box">
                            <div class="gauge-val" id="dynoRpm">2,400</div>
                            <div class="gauge-label">ENGINE RPM</div>
                        </div>
                        <div class="gauge-box">
                            <div class="gauge-val" id="dynoHp">310</div>
                            <div class="gauge-label">HORSEPOWER (WHP)</div>
                        </div>
                        <div class="gauge-box">
                            <div class="gauge-val" id="dynoBoost">1.1 bar</div>
                            <div class="gauge-label">TURBO BOOST</div>
                        </div>
                    </div>
                </div>

                <div style="background:rgba(255,255,255,0.04); border:1px solid var(--border); padding:12px; border-radius:8px; font-size:13px; margin-bottom:15px; text-align:left;">
                    🏁 <strong>Bay Reservation Confirmed:</strong> Dyno Cell #2 is allocated for <span id="confirmedCar" style="color:var(--text); font-weight:700;">BMW M3</span>. Calibration map prepared.
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Finalize & Return to Showcase</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function startDynoSimulation(e) {
    e.preventDefault();
    document.getElementById('dynoBookingStep').style.display = 'none';
    document.getElementById('dynoRunStep').style.display = 'block';
    
    const car = document.getElementById('carModel').value;
    document.getElementById('confirmedCar').textContent = car;
    
    let rpm = 2000;
    let hp = 300;
    let boost = 0.8;
    const bar = document.getElementById('dynoRpmBar');
    const rpmElem = document.getElementById('dynoRpm');
    const hpElem = document.getElementById('dynoHp');
    const boostElem = document.getElementById('dynoBoost');
    const statusElem = document.getElementById('dynoStatus');
    
    const dynoInterval = setInterval(() => {
        if (rpm < 7200) {
            rpm += 260;
            hp += 12;
            boost = (0.8 + (hp / 450) * 1.3).toFixed(1);
            let pct = ((rpm - 2000) / 5200) * 100;
            bar.style.width = pct + '%';
            rpmElem.textContent = rpm.toLocaleString();
            hpElem.textContent = hp + ' WHP';
            boostElem.textContent = boost + ' bar';
        } else {
            clearInterval(dynoInterval);
            statusElem.textContent = 'PULL COMPLETE • MAP VERIFIED ✓';
            statusElem.style.color = '#10b981';
            hpElem.style.color = '#10b981';
        }
    }, 80);
}

function openBookingModal(serviceName) {
    document.getElementById('dynoBookingStep').style.display = 'block';
    document.getElementById('dynoRunStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function startDynoSimulation(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ AutoPro Dyno Simulator installed.")

# -------------------------------------------------------------
# 4. CLEANPRO: Eco Deep Cleaning Crew Allocator & Square Meter Estimator
# -------------------------------------------------------------
def update_cleanpro():
    path = os.path.join(SITE_DIR, "cleanpro/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* CleanPro Crew Allocator */
.crew-step { background: rgba(16,185,129,0.06); border: 1px dashed #10b981; border-radius: 12px; padding: 14px; margin: 15px 0; }
.crew-badges { display: flex; gap: 8px; flex-wrap: wrap; margin-top: 8px; }
.crew-badge { background: #10b981; color:#fff; font-size: 11px; padding: 4px 10px; border-radius: 20px; font-weight: 700; }
"""
    if "/* CleanPro Crew Allocator */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- CleanPro Crew Booking Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 580px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Eco Facility & Home Sanitation Booking</h3>
                    <p class="modal-sub">Certified Green Crew Allocation & HEPA Air Scrubbing</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="cleanFormStep">
                <form onsubmit="handleCleanSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Property Type & Surface Area</label>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                            <select class="form-input" id="propertyType">
                                <option value="Luxury Apartment">Luxury Apartment</option>
                                <option value="Villa / Detached Home">Villa / Detached Home</option>
                                <option value="Commercial Office Space">Commercial Office Space</option>
                                <option value="Post-Construction Clean">Post-Construction Clean</option>
                            </select>
                            <input type="number" class="form-input" id="cleanArea" value="120" placeholder="Area (sqm)" required>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Target Sanitation Date</label>
                        <input type="date" class="form-input" id="cleanDate" value="2026-08-21" required>
                    </div>

                    <div class="form-group">
                        <label class="form-label">Client Name & Phone</label>
                        <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px;">
                            <input type="text" class="form-input" id="cleanClient" value="Mariam Abashidze" required>
                            <input type="tel" class="form-input" id="cleanPhone" value="+995 595 11 22 33" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">✨ Allocate Professional Cleaning Crew ➔</button>
                </form>
            </div>

            <div id="cleanSuccessStep" style="display:none; text-align:center;">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(16,185,129,0.2); color:#10b981; font-size:30px; display:flex; align-items:center; justify-content:center; margin: 0 auto 12px;">✓</div>
                <h3 style="font-size:20px; margin-bottom:5px;">Crew Successfully Assigned!</h3>
                <p style="color:var(--text-muted); font-size:13px; margin-bottom:15px;">Eco-Sanitation Team #3 has locked your reservation.</p>
                
                <div class="crew-step" style="text-align:left;">
                    <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:13px;">
                        <span style="color:var(--text-muted);">Assigned Leader:</span>
                        <strong>Lela Beridze (Team Lead)</strong>
                    </div>
                    <div style="display:flex; justify-content:space-between; margin-bottom:6px; font-size:13px;">
                        <span style="color:var(--text-muted);">Equipment Loadout:</span>
                        <span style="font-weight:700; color:#10b981;">Kärcher Steam + HEPA-14</span>
                    </div>
                    <div class="crew-badges">
                        <span class="crew-badge">🌿 100% Biodegradable</span>
                        <span class="crew-badge">🛡️ Insured Clean</span>
                        <span class="crew-badge">⚡ Same-Day Turnaround</span>
                    </div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Close</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleCleanSubmit(e) {
    e.preventDefault();
    document.getElementById('cleanFormStep').style.display = 'none';
    document.getElementById('cleanSuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('cleanFormStep').style.display = 'block';
    document.getElementById('cleanSuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleCleanSubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ CleanPro Crew allocation system installed.")

# -------------------------------------------------------------
# 5. DENTACARE: 3D Smile Simulator & Dental Consultation Booking
# -------------------------------------------------------------
def update_dentacare():
    path = os.path.join(SITE_DIR, "dentacare/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* DentaCare 3D Smile Simulator */
.denta-scan-box { background: #0c1a2c; border: 1px solid #0ea5e9; border-radius: 12px; padding: 15px; margin: 15px 0; text-align: center; }
.smile-compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 10px; }
.smile-preview-img { width: 100%; height: 110px; object-fit: cover; border-radius: 8px; border: 1px solid rgba(14,165,233,0.3); }
"""
    if "/* DentaCare 3D Smile Simulator */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- DentaCare Digital Consultation Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">3D Guided Dental Consultation & Scan</h3>
                    <p class="modal-sub">CBCT 3D Tomography & Porcelain Veneer Preview</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="dentaFormStep">
                <form onsubmit="handleDentaSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Clinical Treatment Category</label>
                        <select class="form-input" id="dentaProcedure">
                            <option value="All-on-4 / All-on-6 Guided Implantology">All-on-4 / All-on-6 Guided Implantology</option>
                            <option value="E.max Swiss Porcelain Veneers (Full Smile Makeover)">E.max Swiss Porcelain Veneers (Full Smile Makeover)</option>
                            <option value="Invisalign / Clear Aligner Orthodontics">Invisalign / Clear Aligner Orthodontics</option>
                            <option value="Microscopic Root Canal Therapy">Microscopic Root Canal Therapy</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Patient Full Name</label>
                            <input type="text" class="form-input" id="patientName" value="Dr. Sandro Tsitsishvili" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Mobile Contact</label>
                            <input type="tel" class="form-input" id="patientPhone" value="+995 599 44 55 66" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">🦷 Generate 3D Smile Analysis & Book Slot ➔</button>
                </form>
            </div>

            <div id="dentaSuccessStep" style="display:none;">
                <div class="denta-scan-box">
                    <div style="font-size:12px; font-weight:700; color:#0ea5e9; text-transform:uppercase;">CBCT 3D Digital Smile Synthesis</div>
                    <div class="smile-compare-grid">
                        <div>
                            <img src="https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=300&q=80" alt="Before" class="smile-preview-img">
                            <div style="font-size:11px; color:#94a3b8; margin-top:4px;">Diagnostic Scan</div>
                        </div>
                        <div>
                            <img src="https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=300&q=80" alt="After" class="smile-preview-img">
                            <div style="font-size:11px; color:#0ea5e9; margin-top:4px;">3D Veneer Target</div>
                        </div>
                    </div>
                </div>

                <div style="background:rgba(14,165,233,0.08); border-left:3px solid #0ea5e9; padding:10px 14px; border-radius:6px; font-size:13px; margin-bottom:15px;">
                    ✅ <strong>VIP Operatory Scheduled:</strong> Dr. Nicholas V. and surgical suite #1 reserved for patient.
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Return</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleDentaSubmit(e) {
    e.preventDefault();
    document.getElementById('dentaFormStep').style.display = 'none';
    document.getElementById('dentaSuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('dentaFormStep').style.display = 'block';
    document.getElementById('dentaSuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleDentaSubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ DentaCare 3D Smile Simulator installed.")

# -------------------------------------------------------------
# 6. LEGALLINE: Retainer Contract & NDA Signature Simulator
# -------------------------------------------------------------
def update_legalline():
    path = os.path.join(SITE_DIR, "legalline/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* LegalLine Contract Simulator */
.legal-contract-box { background: rgba(212, 175, 55, 0.05); border: 1px solid rgba(212, 175, 55, 0.3); border-radius: 10px; padding: 15px; margin: 15px 0; }
.legal-sig-line { border-bottom: 2px dashed #d4af37; height: 35px; margin: 10px 0; font-family: 'Cinzel', serif; font-style: italic; color: #d4af37; display: flex; align-items: flex-end; padding-bottom: 4px; }
"""
    if "/* LegalLine Contract Simulator */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- LegalLine Retainer & NDA Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Chambers Retainer & Case Evaluation</h3>
                    <p class="modal-sub">Strict Attorney-Client Privilege & NDA Protocol</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="legalFormStep">
                <form onsubmit="handleLegalSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Corporate / Legal Matter Practice Area</label>
                        <select class="form-input" id="legalPractice">
                            <option value="Cross-Border M&A & Tax Arbitration">Cross-Border M&A & Tax Arbitration</option>
                            <option value="Intellectual Property & Technology Protection">Intellectual Property & Technology Protection</option>
                            <option value="Commercial Real Estate Title & Zoning">Commercial Real Estate Title & Zoning</option>
                            <option value="High-Stakes Commercial Litigation">High-Stakes Commercial Litigation</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Entity / Representative</label>
                            <input type="text" class="form-input" id="legalClient" value="Irakli Kvirikashvili (CEO)" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Secure Phone / Signal</label>
                            <input type="tel" class="form-input" id="legalPhone" value="+995 599 77 88 99" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">⚖️ Execute Preliminary NDA & Reserve Senior Partner ➔</button>
                </form>
            </div>

            <div id="legalSuccessStep" style="display:none;">
                <div class="legal-contract-box">
                    <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:700; color:#d4af37;">
                        <span>CONFIDENTIAL ATTORNEY-CLIENT PRIVILEGE</span>
                        <span>DOC-REF #LEG-8849</span>
                    </div>
                    <div style="font-size:13px; margin-top:8px; line-height:1.5; color:var(--text);">
                        Chambers of LegalLine hereby acknowledges receipt of confidential briefing. Managing Senior Partner <strong>Vakhtang Eristavi</strong> assigned.
                    </div>
                    <div class="legal-sig-line">✓ Digitally Encrypted & Sealed: Irakli Kvirikashvili</div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Acknowledge & Close</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleLegalSubmit(e) {
    e.preventDefault();
    document.getElementById('legalFormStep').style.display = 'none';
    document.getElementById('legalSuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('legalFormStep').style.display = 'block';
    document.getElementById('legalSuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleLegalSubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ LegalLine Retainer & NDA system installed.")

# -------------------------------------------------------------
# 7. SAKARTVELO HOMES: Private VIP Penthouse Viewing Scheduler
# -------------------------------------------------------------
def update_sakartvelo_homes():
    path = os.path.join(SITE_DIR, "sakartvelo-homes/index.html")
    with open(path) as f:
        html = f.read()

    modal_html = """<!-- Sakartvelo Homes Private Viewing Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 600px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Schedule VIP Property Tour</h3>
                    <p class="modal-sub">Chauffeured Mercedes-Maybach Viewing & ROI Portfolio Briefing</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="realtyFormStep">
                <form onsubmit="handleRealtySubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Estate / Penthouse Selection</label>
                        <select class="form-input" id="realtyEstate">
                            <option value="Vake Crown Penthouse (450 sqm, Infinity Pool)">Vake Crown Penthouse (450 sqm, Infinity Pool)</option>
                            <option value="Mtatsminda View Villa (680 sqm, Wine Cellar)">Mtatsminda View Villa (680 sqm, Wine Cellar)</option>
                            <option value="Batumi Riviera Sea-View Tower (Level 38)">Batumi Riviera Sea-View Tower (Level 38)</option>
                            <option value="Old Tbilisi Heritage Mansion Restored">Old Tbilisi Heritage Mansion Restored</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Investor / Buyer Name</label>
                            <input type="text" class="form-input" id="buyerName" value="Alexandre Dumas-Loria" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Direct Phone / WhatsApp</label>
                            <input type="tel" class="form-input" id="buyerPhone" value="+995 591 00 11 22" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">🏛️ Reserve Private Chauffeured Inspection ➔</button>
                </form>
            </div>

            <div id="realtySuccessStep" style="display:none; text-align:center;">
                <div style="width:60px; height:60px; border-radius:50%; background:rgba(212,175,55,0.2); color:#d4af37; font-size:30px; display:flex; align-items:center; justify-content:center; margin: 0 auto 12px;">✓</div>
                <h3 style="font-size:20px; margin-bottom:5px;">Private Viewing Confirmed</h3>
                <p style="color:var(--text-muted); font-size:13px; margin-bottom:15px;">Senior Partner Broker <strong>Nata Kipiani</strong> will meet you with full deeds & yield audits.</p>
                
                <div style="background:rgba(255,255,255,0.04); border:1px solid var(--border); border-radius:10px; padding:12px; text-align:left; font-size:13px; margin-bottom:15px;">
                    <div style="color:var(--text-muted); font-size:11px;">CONCIERGE AMENITY:</div>
                    <div style="font-weight:700; color:#d4af37;">Private Maybach Pick-Up Arranged</div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Return</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleRealtySubmit(e) {
    e.preventDefault();
    document.getElementById('realtyFormStep').style.display = 'none';
    document.getElementById('realtySuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('realtyFormStep').style.display = 'block';
    document.getElementById('realtySuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleRealtySubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ Sakartvelo Homes VIP Viewing system installed.")

# -------------------------------------------------------------
# 8. IRONFORGE: Biohacking Recovery Chamber & Athletic Pass Generator
# -------------------------------------------------------------
def update_ironforge():
    path = os.path.join(SITE_DIR, "ironforge/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* IronForge Biohacking Pass */
.forge-pass { background: linear-gradient(135deg, #14161c, #0a0b0e); border: 2px solid #ef4444; border-radius: 12px; padding: 15px; margin: 15px 0; position: relative; text-align: left; }
.forge-barcode { font-family: monospace; letter-spacing: 4px; color: #ef4444; font-weight: 900; margin-top: 10px; }
"""
    if "/* IronForge Biohacking Pass */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- IronForge Pass Generator Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 580px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Athletic Pass & Biohacking Chamber Booking</h3>
                    <p class="modal-sub">Cryotherapy (-110°C), Hyperbaric Oxygen & Heavy Lifting</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="forgeFormStep">
                <form onsubmit="handleForgeSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Recovery or Strength Tier</label>
                        <select class="form-input" id="forgeTier">
                            <option value="Pro Athlete All-Access + Cryo Recovery (Daily)">Pro Athlete All-Access + Cryo Recovery (Daily)</option>
                            <option value="Biohacking Recovery Chamber 10-Session Pass">Biohacking Recovery Chamber 10-Session Pass</option>
                            <option value="Powerlifting & Strongman Platform VIP">Powerlifting & Strongman Platform VIP</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Athlete Name</label>
                            <input type="text" class="form-input" id="athleteName" value="Levan Saginashvili" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Phone / WhatsApp</label>
                            <input type="tel" class="form-input" id="athletePhone" value="+995 555 10 20 30" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">⚡ Generate Instant Access RFID Pass ➔</button>
                </form>
            </div>

            <div id="forgeSuccessStep" style="display:none;">
                <div class="forge-pass">
                    <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:800; color:#ef4444;">
                        <span>IRONFORGE ATHLETICS CLUB</span>
                        <span>RFID PASS: ACTIVE</span>
                    </div>
                    <div style="font-size:16px; font-weight:800; margin-top:8px;" id="dispAthleteName">Levan Saginashvili</div>
                    <div style="font-size:12px; color:#94a3b8;">Biometric Chamber Access Granted • Turnstile Unlock Enabled</div>
                    <div class="forge-barcode">||| |||| | |||||| || | |||| ||||</div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Return to Club</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleForgeSubmit(e) {
    e.preventDefault();
    document.getElementById('dispAthleteName').textContent = document.getElementById('athleteName').value;
    document.getElementById('forgeFormStep').style.display = 'none';
    document.getElementById('forgeSuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('forgeFormStep').style.display = 'block';
    document.getElementById('forgeSuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleForgeSubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ IronForge Biohacking Pass Generator installed.")

# -------------------------------------------------------------
# 9. SWEETEST HOUSE: Artisanal Cake Pre-Order & Oven Tracker
# -------------------------------------------------------------
def update_sweetest_house():
    path = os.path.join(SITE_DIR, "sweetest-house/index.html")
    with open(path) as f:
        html = f.read()

    modal_html = """<!-- Sweetest House Artisanal Pre-Order Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 580px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Artisanal Pâtisserie Pre-Order</h3>
                    <p class="modal-sub">Fresh Batch French Viennoiserie & Custom Gateau</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="bakeryFormStep">
                <form onsubmit="handleBakerySubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Pastry Selection / Custom Order</label>
                        <select class="form-input" id="pastryItem">
                            <option value="French Butter Croissant Box (6 pcs) + Pistachio Cream">French Butter Croissant Box (6 pcs) + Pistachio Cream</option>
                            <option value="Grand Cru Valrhona Chocolate & Hazelnut Praliné Cake">Grand Cru Valrhona Chocolate & Hazelnut Praliné Cake</option>
                            <option value="Madagascar Vanilla Mille-Feuille Celebration Tart">Madagascar Vanilla Mille-Feuille Celebration Tart</option>
                            <option value="San Sebastián Burnt Basque Cheesecake">San Sebastián Burnt Basque Cheesecake</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Guest Name</label>
                            <input type="text" class="form-input" id="bakeryName" value="Nino Chavchavadze" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Pickup Date / Time</label>
                            <input type="datetime-local" class="form-input" id="bakeryTime" value="2026-08-21T09:00" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">🥐 Reserve Fresh Bakery Batch ➔</button>
                </form>
            </div>

            <div id="bakerySuccessStep" style="display:none; text-align:center;">
                <div style="font-size:36px; margin-bottom:5px;">🥖🔥</div>
                <h3 style="font-size:20px; margin-bottom:5px;">Oven Slot Scheduled!</h3>
                <p style="color:var(--text-muted); font-size:13px; margin-bottom:15px;">Your order is queued for morning baking with Normandy butter.</p>
                
                <div style="background:rgba(217,119,6,0.08); border:1px solid rgba(217,119,6,0.3); border-radius:10px; padding:12px; font-size:13px; margin-bottom:15px; text-align:left;">
                    <div style="color:var(--text-muted); font-size:11px;">PICKUP LOCATION:</div>
                    <div style="font-weight:700;">Sweetest House Atelier • Barnov St. 14, Vera</div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Return to Menu</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleBakerySubmit(e) {
    e.preventDefault();
    document.getElementById('bakeryFormStep').style.display = 'none';
    document.getElementById('bakerySuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('bakeryFormStep').style.display = 'block';
    document.getElementById('bakerySuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleBakerySubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ Sweetest House Bakery pre-order installed.")

# -------------------------------------------------------------
# 10. TECHFIX: Hardware Diagnostic Scanner & IMEI Repair Status Tracker
# -------------------------------------------------------------
def update_techfix():
    path = os.path.join(SITE_DIR, "techfix/index.html")
    with open(path) as f:
        html = f.read()

    styles = """
/* TechFix Diagnostics */
.tech-diag-box { background: #070d18; border: 1px solid #3b82f6; border-radius: 10px; padding: 14px; margin: 15px 0; }
.diag-log-line { font-family: monospace; font-size: 12px; color: #3b82f6; margin-bottom: 4px; }
"""
    if "/* TechFix Diagnostics */" not in html:
        html = html.replace("</style>", f"{styles}
</style>")

    modal_html = """<!-- TechFix Hardware Diagnostic & Repair Tracker Modal -->
    <div class="modal-backdrop" id="bookingModal" onclick="if(event.target===this)closeBookingModal()">
        <div class="modal-card" style="max-width: 580px;">
            <div class="modal-header">
                <div>
                    <h3 class="modal-title" id="modalTitle">Micro-Soldering Lab Diagnostics & Queue</h3>
                    <p class="modal-sub">Thermal Camera Inspection & Board-Level Repair Ticket</p>
                </div>
                <button class="modal-close" onclick="closeBookingModal()" aria-label="Close modal">&times;</button>
            </div>
            
            <div id="techFormStep">
                <form onsubmit="handleTechSubmit(event)">
                    <div class="form-group">
                        <label class="form-label">Device Type & Problem</label>
                        <select class="form-input" id="techDevice">
                            <option value="iPhone 15/16 Pro Max - NAND / Power IC Reballing">iPhone 15/16 Pro Max - NAND / Power IC Reballing</option>
                            <option value="MacBook Pro M-Series - Liquid Damage Ultrasonic Clean">MacBook Pro M-Series - Liquid Damage Ultrasonic Clean</option>
                            <option value="iPad Pro - Micro-Jumper Trace Repair">iPad Pro - Micro-Jumper Trace Repair</option>
                            <option value="Samsung Galaxy Ultra - OLED Layer Lamination">Samsung Galaxy Ultra - OLED Layer Lamination</option>
                        </select>
                    </div>

                    <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                        <div class="form-group">
                            <label class="form-label">Customer Name</label>
                            <input type="text" class="form-input" id="techCustomer" value="Giorgi Tsereteli" required>
                        </div>
                        <div class="form-group">
                            <label class="form-label">Phone Contact</label>
                            <input type="tel" class="form-input" id="techPhone" value="+995 598 22 33 44" required>
                        </div>
                    </div>

                    <button type="submit" class="modal-submit-btn">⚡ Run Hardware Diagnostic & Create Ticket ➔</button>
                </form>
            </div>

            <div id="techSuccessStep" style="display:none;">
                <div class="tech-diag-box">
                    <div style="display:flex; justify-content:space-between; font-size:12px; font-weight:700; color:#3b82f6; margin-bottom:8px;">
                        <span>MICROSCOPE LAB TELEMETRY</span>
                        <span>TICKET #TX-5092</span>
                    </div>
                    <div class="diag-log-line">✓ Oscilloscope VCC_MAIN Voltage Check: PASSED</div>
                    <div class="diag-log-line">✓ Thermal Cam Hotspot Analysis: 0.04A short located</div>
                    <div class="diag-log-line" style="color:#10b981;">✓ Micro-Soldering Station #4 Reserved</div>
                </div>

                <button type="button" class="btn btn-primary" style="width:100%;" onclick="closeBookingModal()">Done & Return to Lab</button>
            </div>
        </div>
    </div>"""

    old_modal = re.search(r'<div class="modal-backdrop" id="bookingModal".*?</form>\s*</div>\s*</div>', html, re.S)
    if old_modal:
        html = html.replace(old_modal.group(0), modal_html)

    js_code = """
function handleTechSubmit(e) {
    e.preventDefault();
    document.getElementById('techFormStep').style.display = 'none';
    document.getElementById('techSuccessStep').style.display = 'block';
}

function openBookingModal(serviceName) {
    document.getElementById('techFormStep').style.display = 'block';
    document.getElementById('techSuccessStep').style.display = 'none';
    document.getElementById('bookingModal').classList.add('show');
}
"""
    if "function handleTechSubmit(" not in html:
        html = html.replace("function openBookingModal(", f"{js_code}
function _orig_openBookingModal(")

    with open(path, "w") as f:
        f.write(html)
    print("✓ TechFix Diagnostic Tracker installed.")

def sync_to_pro():
    for folder in os.listdir(SITE_DIR):
        src = os.path.join(SITE_DIR, folder)
        dst = os.path.join(PRO_DIR, folder)
        if os.path.isdir(src) and os.path.exists(dst):
            src_file = os.path.join(src, "index.html")
            dst_file = os.path.join(dst, "index.html")
            if os.path.exists(src_file):
                shutil.copy2(src_file, dst_file)
    print("✓ All index files synced to gallery-sites-pro.")

update_glowup()
update_aquafix()
update_autopro()
update_cleanpro()
update_dentacare()
update_legalline()
update_sakartvelo_homes()
update_ironforge()
update_sweetest_house()
update_techfix()
sync_to_pro()
print("🎉 All 10 demo sites successfully upgraded with rich simulated action systems!")
