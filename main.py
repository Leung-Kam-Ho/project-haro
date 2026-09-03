import libtmux

if __name__ == "__main__":
    svr = libtmux.Server()
    if not svr.has_session("haro"):
        haro_session = svr.new_session(session_name="haro")
    else:
        haro_session = svr.sessions.get(session_name="haro")
    window = haro_session.active_window
    panel = window.active_pane
    panel.send_keys("echo hello", enter=True)  # Send Ctrl+C to stop any running process
    print(svr)
    print(haro_session)
    # kill-session
    haro_session.kill()  # Kill the session
