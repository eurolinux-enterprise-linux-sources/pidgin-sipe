Name:           pidgin-sipe
Version:        1.20.1
Release:        2%{?dist}
Summary:        Pidgin protocol plugin to connect to MS Office Communicator

Group:          Applications/Internet
License:        GPLv2+
URL:            http://sipe.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/sipe/sipe/pidgin-sipe-%{version}/pidgin-sipe-%{version}.tar.bz2

BuildRequires:  pkgconfig(glib-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.12.0
BuildRequires:  pkgconfig(gstreamer-0.10)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nice) >= 0.1.0
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(purple) >= 2.8.0
BuildRequires:  krb5-devel, libtool, intltool, gettext

Requires:       purple-sipe = %{version}-%{release}


%description
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)
    * Reuters Messaging

With this plugin you should be able to replace your Microsoft Office
Communicator client with Pidgin.

This package provides the icon set for Pidgin.


%package -n purple-sipe
Summary:        Libpurple protocol plugin to connect to MS Office Communicator
Group:          Applications/Internet
License:        GPLv2+


%description -n purple-sipe
A third-party plugin for the Pidgin multi-protocol instant messenger.
It implements the extended version of SIP/SIMPLE used by various products:

    * Skype for Business
    * Microsoft Office 365
    * Microsoft Business Productivity Online Suite (BPOS)
    * Microsoft Lync Server
    * Microsoft Lync Server 2010
    * Microsoft Office Communications Server (OCS 2007/2007 R2)
    * Microsoft Live Communications Server (LCS 2003/2005)
    * Reuters Messaging

This package provides the protocol plugin for libpurple clients.


%prep
%setup -q

%build
%configure \
    --with-krb5 \
    --enable-purple \
    --disable-telepathy
make %{?_smp_mflags}
make %{?_smp_mflags} check


%install
%makeinstall
find %{buildroot} -type f -name "*.la" -delete -print
# Pidgin doesn't have 24 or 32 pixel icons
rm -f \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/24/sipe.png \
   %{buildroot}%{_datadir}/pixmaps/pidgin/protocols/32/sipe.png
%find_lang %{name}


%clean
rm -rf %{buildroot}


%files -n purple-sipe -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/purple-2/libsipe.so


%files
%defattr(-,root,root,-)
%{_datadir}/pixmaps/pidgin/protocols/*/sipe.*


%changelog
* Tue Apr 12 2016 Debarshi Ray <rishi@fedoraproject.org> - 1.20.1-2
- Bump release to be higher than the EPEL build
Resolves: #1297461

* Sat Oct 24 2015 Stefan Becker <chemobejk@gmail.com> - 1.20.1-1
- update to 1.20.1:
    - add support for another type of ADFS response
    - improve configure check for back-ported features

* Sat Aug 29 2015 Stefan Becker <chemobejk@gmail.com> - 1.20.0-1
- update to 1.20.0:
    - add support for SRTP (requires libpurple >= 3.0.0)
    - parse HTML from Lync conference URL
    - fixes Office365 authentication failure (bz #1257485)

* Sat Apr 04 2015 Stefan Becker <chemobejk@gmail.com> - 1.19.1-1
- update to 1.19.1:
    - add workaround for farstream 0.1.x with libnice >= 0.1.10
    - fix SIP re-authentication timeout to be max. 8 hours

* Sat Feb 07 2015 Stefan Becker <chemobejk@gmail.com> - 1.19.0-1
- update to 1.19.0:
    - added support for automatic authentication scheme selection
    - added support for Multi-Factor Authentication (MFA)
    - added support for buddy photos from contact card
    - added support for SIP ID in contact search
    - added support for EWS based contact search when UCS is used
    - improves user experience for [MS-DLX] based contact search
    - fixes calendar state machine when EWS URL is set

* Mon Dec 29 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.5-1
- update to 1.18.5:
    - fixes Pidgin user status being stuck in "Away"
    - fixes RealmInfo request when user and login name differ

* Sat Oct 18 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.4-1
- update to 1.18.4:
    - fixes ADFS failure when user and login name differ
    - fixes a longstanding issue that the Pidgin user status sometimes
      didn't switch back to "Available" after the end of a meeting
    - fixes some memory leaks

* Sat Aug 16 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.3-1
- update to 1.18.3:
    - fixes audio/video call if host has IPv6 address (bz #1124510)
    - fixes assert triggered by EWS autodiscover in older libxml2 versions
    - fixes crash triggered by EWS autodiscover when glib2 < 2.30.0

* Sat Jun 07 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.2-1
- update to 1.18.2:
    - fixes crash when PersistentChat sends BYE
    - fixes joining of conference for some users
    - fixes conference call ending in error message
    - fixes EWS autodiscover for some Office 365 users
    - UCS now honors email URL set by user

* Sat Apr 12 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.1-1
- update to 1.18.1:
    - fixes crash when gstreamer nice plugin is missing (bz #1071710)
    - fixes false "not delivered" errors in conference
    - fixes incorrect HTML escaping for URLs
    - fixes conference call ending in error message
    - fixes endless loop with failed HTTP Basic authentication
    - fixes EWS autodiscover for some Office 365 users
    - fixes missing "Copy to" in buddy menu

* Sun Mar 09 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.0-2
- Fedora Packaging Guidelines: use pkgconfig() for BRs

* Sat Jan 11 2014 Stefan Becker <chemobejk@gmail.com> - 1.18.0-1
- update to 1.18.0:
    - added support for EWS Autodiscover redirection

* Wed Dec 11 2013 Stefan Becker <chemobejk@gmail.com> - 1.17.3-1
- update to 1.17.3:
    - fixes crash when groupchat session expired (again)
    - fixes HTTP re-authentication with NTLM
    - fixes UCS Persona key extraction

* Sat Nov 30 2013 Stefan Becker <chemobejk@gmail.com> - 1.17.2-1
- update to 1.17.2:
    - fixes problems with typing notifications fix (bz #1031554)
    - fixes crash when groupchat session expired

* Sat Nov 16 2013 Stefan Becker <chemobejk@gmail.com> - 1.17.1-1
- update to 1.17.1:
    - fixes typing notifications
    - fixes that passwords were not entity encoded
    - accept alternatives for webticket timestamp/keydata

* Sat Sep 21 2013 Stefan Becker <chemobejk@gmail.com> - 1.17.0-1
- update to 1.17.0:
    - added Lync 2013 support: buddy list modification, buddy photo, group chat
    - added support for group chat history
    - fixes group chat: duplicate messages & users, HTML tags in text
    - fixes EWS autodiscover for Office 365

* Sat Jul 13 2013 Stefan Becker <chemobejk@gmail.com> - 1.16.1-1
- update to 1.16.1: bug fix release
    - fixes call failure when host has multiple IP addresses
    - fixes buddy list handling after moving to Lync 2013
    - fixes crashes in new HTTP stack

* Sat Jun 15 2013 Stefan Becker <chemobejk@gmail.com> - 1.16.0-1
- update to 1.16.0:
    - new HTTP stack: reduced network traffic, no more crashes
    - added support to call to a phone number
    - fixes subscription timeout handling, e.g. for buddy status updates

* Sun Apr 07 2013 Stefan Becker <chemobejk@gmail.com> - 1.15.1-1
- update to 1.15.1: bug fix release
    - fixes crash experienced by some users (bz #928323)
    - fixes broken NTLM fallback in Negotiate

* Sat Mar 09 2013 Stefan Becker <chemobejk@gmail.com> - 1.15.0-1
- update to 1.15.0:
    - added support for Kerberos & Negotiate authentication in HTTP connections
    - added support for DNS A record search in server auto-discovery
    - added setting to suppress calendar information publishing
    - unified Single Sign-On (SSO) handling in all places

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 26 2012 Stefan Becker <chemobejk@gmail.com> - 1.14.1-1
- update to 1.14.1: bug fix release

* Sun Dec 16 2012 Stefan Becker <chemobejk@gmail.com> - 1.14.0-1
- update to 1.14.0:
    - added support for Web Ticket authentication using ADFS
    - added support for buddy photos
    - added support for call to Audio Test Service
    - reduced network traffic for acquiring Web Tickets

* Sun Aug 19 2012 Stefan Becker <chemobejk@gmail.com> - 1.13.3-1
- update to 1.13.3: bug fix release

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 10 2012 Stefan Becker <chemobejk@gmail.com> - 1.13.2-1
- update to 1.13.2: bug fix release

* Mon Apr 09 2012 Stefan Becker <chemobejk@gmail.com> - 1.13.1-1
- update to 1.13.1: bug fix release
- drop obsolete patch for GCC 4.7.0 compilation errors

* Wed Mar 14 2012 Stefan Becker <chemobejk@gmail.com> - 1.13.0-2
- add patch to fix maybe-uninitialized errors for F17+

* Wed Mar 14 2012 Stefan Becker <chemobejk@gmail.com> - 1.13.0-1
- update to 1.13.0:
    - support for Lync & Office365
    - added [MS-SIPAE] TLS-DSK authentication scheme
    - added [MS-DLX] based Get Info/Contact Search
    - added experimental media TCP transport
- add BR nss-devel
- drop obsolete patch to replace deprecated glib2 functions

* Mon Jan 09 2012 Stefan Becker <chemobejk@gmail.com> - 1.12.0-3
- add patch to replace deprecated glib2 functions for F17+

* Sun Jan 08 2012 Stefan Becker <chemobejk@gmail.com> - 1.12.0-2
- enable audio/video call support for F15+ (bz #761528)

* Mon Sep 12 2011 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0:
    - Add support for OCS2007R2 Group Chat
    - Miscellaneous features and bugfixes

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.11.2-1
- Update to 1.11.2

* Wed Oct 06 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Fri Sep 24 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-2
- Fix group for purple-sipe (#624246)

* Fri Jul 16 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.10.1-1
- Upstream 1.10.1:
        - Fixes to build against pidgin-2.7
        - Initial support for Office 2007+ "Access Levels"
        - SVG icon artwork
        - Miscellaneous bugfixes

* Tue Mar 16 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.9.1-1
- Upstream 1.9.1:
        - Fix Kerberos authentication for unix platforms (broken in 1.9.0)
        - Bugfixes

* Thu Mar 11 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.9.0-1
- Upstream 1.9.0:
        - Contributed File transfer functionality. File encryption is supported.
        - NTLMv2 and NTLMv2 Session Security support
        - Implemented SIP Authentication Extensions protocol version 4 and 3
        - another shot at presence update problems
        - fix crash caused by uninitialized security contexts
        - Updated translations: ru, de, es, pt_BR
        - Bugfixes and crash fixes
- BR libpurple >= 2.4.0
- Split into purple-sipe and pidgin-sipe
- Other spec fixes to match upstream's spec file

* Tue Feb 16 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.8.1-1
- Upstream 1.8.1 (crash fixes)

* Mon Feb 08 2010 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.8.0-1
- Upstream 1.8.0 (new features)
- Exchange Calendar integration
- New and updated translations
- Bugfixes

* Mon Nov 23 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.7.1-1
- Upstream 1.7.1 (bugfixes)

* Tue Nov 03 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.7.0-1
- Upstream 1.7.0

* Mon Sep 28 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6.3-1
- Upstream 1.6.3

* Tue Sep 08 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6.2-1
- Upstream 1.6.2
- Drop obsoleted ppc fix patch

* Fri Jul 31 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6.0-2
- Add BR: gettext to build on EPEL

* Thu Jul 30 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6.0-2
- Another attempt at ppc build fix (patch from Stefan Becker)

* Tue Jul 28 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.6.0-1
- Upstream 1.6.0
- Build on ppc, but pass --enable-quality-check=no to configure

* Thu Jul 16 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.5.0-2
- Build --with-krb5

* Tue Jun 30 2009 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.5.0-1
- Initial packaging.

