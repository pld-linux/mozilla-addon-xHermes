Summary:	Web2mail support interface
Summary(pl):	Narzêdzie do obs³ugi poczty przez www
Name:		mozilla-addon-xHermes
%define		_realname	xhermes
%define	bver	0.3
%define	pver	pre1
Version:	%{bver}%{pver}
%define	fver	%(echo %{bver} | tr -d .)-%{pver}
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.us-east1.mozdev.org/hermes/xHermes%{fver}.xpi
# Source0-md5:	d6c33a108803ac9d6d287de8cec0f728
Source1:	%{_realname}-installed-chrome.txt
URL:		http://hermes.mozdev.org/
BuildRequires:	unzip
BuildRequires:	zip
Requires(post,postun):	mozilla
Requires(post,postun):	textutils
Requires:	mozilla >= 1.0-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

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

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt ||:
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf} ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom ||:
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome ||:

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt
rm -f %{_libdir}/mozilla/components/{compreg,xpti}.dat \
	%{_datadir}/mozilla/chrome/{chrome.rdf,overlayinfo/*/*/*.rdf}
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regxpcom
MOZILLA_FIVE_HOME=%{_libdir}/mozilla %{_bindir}/regchrome

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
