Summary:	Web2mail support interface
Summary(pl):	Narz�dzie do obs�ugi poczty przez www
Name:		mozilla-addon-xHermes
%define		_realname	xhermes
%define	bver	0.3
%define	pver	pre1
Version:	%{bver}%{pver}
%define	fver	%(echo %{bver} | tr -d .)-%{pver}
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/hermes/xHermes%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://hermes.mozdev.org/
BuildRequires:	unzip
Requires:	mozilla >= 1.0
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Web2mail support interface. It supports mail, internet banking,
sending SMSs, auction serveces accessible through WWW. It can
integrate with sidebar or work in separate window.

%description -l pl
Narz�dzie do obs�ugi poczty, kont bankowych, wysy�ania sms-�w oraz
serwis�w aukcyjnych przez www. Dzia�a jako aplikacja w osobnym
okienku, lub integruje si� z sidebarem.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}
rm -f $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/content/services/bank/*~
rm -f $RPM_BUILD_ROOT%{_chromedir}/%{_realname}/locale/pl-PL/*~

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_chromedir}
cat %{_realname}-installed-chrome.txt >> installed-chrome.txt

%postun
cd %{_chromedir}
cat installed-chrome.txt | grep -v "%{_realname}" > installed-chrome.txt.tmp
cat installed-chrome.txt.tmp > installed-chrome.txt
rm -f installed-chrome.txt.tmp

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}
%{_chromedir}/%{_realname}-installed-chrome.txt
