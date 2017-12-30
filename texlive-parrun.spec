# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/parrun
# catalog-date 2009-09-20 00:02:29 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-parrun
Version:	20170414
Release:	1
Summary:	Typesets (two) streams of text running parallel
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/parrun
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/parrun.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
For typesetting translated text and the original source,
parallel on the same page, one above the other.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/parrun/parrun.sty
%doc %{_texmfdistdir}/doc/latex/parrun/parrun.pdf
%doc %{_texmfdistdir}/doc/latex/parrun/readme
#- source
%doc %{_texmfdistdir}/source/latex/parrun/parrun.dtx
%doc %{_texmfdistdir}/source/latex/parrun/parrun.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090920-2
+ Revision: 754646
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090920-1
+ Revision: 719198
- texlive-parrun
- texlive-parrun
- texlive-parrun
- texlive-parrun

