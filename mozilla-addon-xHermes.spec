Summary:	Web2mail support interface
Summary(pl):	Narzêdzie do obs³ugi poczty przez www
Name:		mozilla-addon-xHermes
%define		_realname	xhermes
%define	bver	0.3
%define	pver	pre1
Version:	%{bver}%{pver}
%define	fver	%(echo %{bver} | tr -d .)-%{pver}
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/hermes/xHermes%{fver}.xpi
Source1:	%{_realname}-installed-chrome.txt
URL:		http://hermes.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_chromedir	%{_libdir}/mozilla/chrome

%description
Web2mail support interface. It supports mail, internet banking,
sending SMSs, auction serveces accessible through WWW. It can
integrate with sidebar or work in separate window.

%description -l pl
Narzêdzie do obs³ugi poczty, kont bankowych, wysy³ania sms-ów oraz
serwisów aukcyjnych przez www. Dzia³a jako aplikacja w osobnym
okienku, lub integruje siê z sidebarem.

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

cd %{_realname}
rm content/services/bank/*~
rm locale/pl-PL/*~
zip -r -9 -m ../%{_realname}.jar ./
cd -

install %{_realname}.jar $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
