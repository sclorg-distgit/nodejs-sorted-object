%{?scl:%scl_package nodejs-sorted-object}
%{!?scl:%global pkg_name %{name}}

%nodejs_find_provides_and_requires
Name:           %{?scl_prefix}nodejs-sorted-object
Version:        1.0.0
Release:        3%{?dist}
Summary:        Returns a copy of an object with its keys sorted
License:        WTFPL
Group:          Development/Languages/Other
Url:            https://github.com/domenic/sorted-object
Source:         http://registry.npmjs.org/sorted-object/-/sorted-object-%{version}.tgz
BuildRequires:  nodejs010
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
Although objects in JavaScript are theoretically unsorted, in practice most engines use insertion order—at least, ignoring numeric keys. This manifests itself most prominently when dealing with an object's JSON serialization. 

So, for example, you might be trying to serialize some object to a JSON file. But every time you write it, it ends up being output in a different order, depending on how you created it in the first place! This makes for some ugly diffs.

sorted-object gives you the answer. Just use this package to create a version of your object with its keys sorted before serializing, and you'll get a consistent order every time.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/sorted-object
cp -pr package.json lib \
        %{buildroot}%{nodejs_sitelib}/sorted-object/

%files
%defattr(-,root,root,-)
%doc README.md LICENSE.txt
%{nodejs_sitelib}/sorted-object

%changelog
* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Remove undefined macro

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-2
- Enable software collection support

* Mon Jan 12 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-1
- Initial build
